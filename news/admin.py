from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post, Category, Author, Comment


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ("title", "author", "rating", "get_cats")
    list_filter = ('title', 'author', 'rating') # добавляем примитивные фильтры в нашу админку
    # list_display = [field.name for field in Post._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    search_fields = ('title', 'author__name__username') # тут всё очень похоже на фильтры из запросов в базу
    # search_fields = ('title', 'author__name') # тут всё очень похоже на фильтры из запросов в базу

    def get_cats(self, obj):
        return ",\n".join([c.name for c in obj.category.all()])
 
admin.site.register(Post, PostAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "get_subscribers_quantity", "get_post_quantity")
    actions = ['empty_category']

    def get_subscribers_quantity(self, obj):
        return obj.subscribers.count()

    def get_post_quantity(self, obj):
        return obj.post_set.all().count()
    
    def empty_category(self, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
        if 'apply' in request.POST:
        # The user clicked submit on the intermediate form.
        # Perform our action:
        # TODO: не работает как надо, удаляет что-то не то
            for q in queryset:
                q.post_set.all().delete()
            
            self.message_user(request,
                              "Удалено {} постов".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())
        
        posts = []
        for q in queryset:
            posts.append(q.post_set.all())
        return render(request,
            'admin/empty_category.html',
            context={
                "category": queryset
            }
        )
    # for q in queryset:
    #     q.post_set.all().delete()
    empty_category.short_description = 'Удалить посты в категории' # описание для более понятного представления в админ панеле задаётся, как будто это объект


admin.site.register(Category, CategoryAdmin)

# Register your models here.
#admin.site.unregister(Post)
#admin.site.register(Category)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "rating")
    search_fields = ('name__username',)

admin.site.register(Author, AuthorAdmin)

#admin.site.register(Author)
admin.site.register(Comment)