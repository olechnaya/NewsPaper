from django.dispatch import receiver # импорт функции получателя @receiver(сигнал, отправитель)
from django.db.models.signals import post_save
from django.core.mail import send_mail

from .models import Post

@receiver(post_save, sender=Post)
def notify_subscribers_about_PostCreatedOrEdited(sender, instance, created, **kwargs):
    # sender - модель, которая активирует сигнал. в данном случае это модель  Post.
    # instance созданная/сохраняемая сущность модели Post
    # created - есть ли эта сущность на данный момент в БД.
    # Если сущность создается - отправляется одно, если изменяется, то отправляется другое
    if created:
        subject = f'Создание поста: {instance.title} от автора {instance.author.name}'
    else:
        subject = f'Пост откорректирован: {instance.title} {instance.date.strftime("%d %m %Y")}'
    
    # взять id категории(ий) созданного поста
    # обратиться к news_category_subscribers  через id  категории(ий) взять id подписанных пользователей
    # взять их почты и сформировать list

    send_mail(
        subject=instance.title,
        message=instance.text,
        from_email="kozhinova.olka@yandex.ru",
        recipient_list=["data19101988@gmail.com",],
    )
    print(subject)