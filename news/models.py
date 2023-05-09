from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User


class Author(models.Model):
    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)
    
    def update_rating(self):
        postRating = self.post_set.all().aggregate(post_rating=Sum("rating"))['post_rating'] or 0
        commentRating = self.name.comment_set.all().aggregate(comment_rating=Sum("rating"))['comment_rating'] or 0
        # ver1
        # postCommentRating = self.post_set.all().aggregate(comment_rating=Sum("rating"))['comment_rating'] or 0
        # ver2
        postCommentRating = Comment.objects.filter(commentPost__author=self).aggregate(Sum('rating')).get('rating__sum')

        self.rating = postRating * 3 + commentRating + postCommentRating
        self.save()
    
    def __str__(self):        
            return self.name.username

class Category(models.Model):
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
    name = models.CharField(max_length=64, unique=True, default="")
    def __str__(self):
        return self.name

class Post(models.Model):
    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
    article = "ART"
    news = "NWS"

    TYPE = [
        (article, "Статья"),
        (news, "Новости"),
    ]
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    postType = models.CharField(max_length=20, choices=TYPE, default=article)
    dateCreation = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0.0)

    def __str__(self):
        return self.title

    # Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу.
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    # Метод preview() возвращает начало статьи (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
    def preview(self):
        return "".join((self.text[0:124],'...'))


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    # commentUser = models.ForeignKey(User)
    text = models.TextField(max_length=512)
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0.0)

    # как добраться до промежуточных моделей
    # вывод имени автора

    def __str__(self):
        try:
            return self.commentPost.author.name.userName
        except:
            return self.commentUser.username

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
