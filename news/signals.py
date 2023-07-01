from django.dispatch import receiver # импорт функции получателя @receiver(сигнал, отправитель)
from django.db.models.signals import m2m_changed
from django.core.mail import send_mail
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import Post

def get_subscribers(category):
    user_email=[]
    for user in category.subscribers.all():
        user_email.append(user.email)
    return user_email


# @receiver(post_save, sender=Post) - не позволяет отлавливать категории, они создаются после его срабатывания
@receiver(m2m_changed, sender=Post.category.through)
def notify_subscribers_about_PostCreatedOrEdited(sender, instance, action, **kwargs):
    # sender - модель, которая активирует сигнал. в данном случае это модель  Post.
    # instance созданная/сохраняемая сущность модели Post
    # created - есть ли эта сущность на данный момент в БД.
    # Если сущность создается - отправляется одно, если изменяется, то отправляется другое
    if action == 'post_add':
        subject = f'Создание поста: {instance.title} от автора {instance.author.name}'
        short_text = instance.text[0:150]
        categories = instance.category.all()
        for c in categories:
            subscribers_mail = get_subscribers(c)
            send_mail(
                subject=f'{subject} в категории {c}',
                message=short_text,
                from_email="kozhinova.olka@yandex.ru",
                recipient_list=subscribers_mail,
            )
    # else:
    #     subject = f'Пост откорректирован: {instance.title} {instance.date.strftime("%d %m %Y")}'
    
    # взять id категории(ий) созданного поста
    # обратиться к news_category_subscribers  через id  категории(ий) взять id подписанных пользователей
    # взять их почты и сформировать list

    
    

    