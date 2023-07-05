from django.dispatch import receiver # импорт функции получателя @receiver(сигнал, отправитель)
from django.db.models.signals import m2m_changed

from .models import Post
from .tasks import new_post_subscription_notification

@receiver(m2m_changed, sender=Post.category.through) # sender=PostCategory - в видосе 1:11:00

def notify_subscribers_about_PostCreatedOrEdited(sender, instance, action, **kwargs):
    if action == 'post_add':
        new_post_subscription_notification(instance)
            

# НЕ РАБОТАЕТ !!!!!!!!!!
#@receiver(post_save, sender=Post) - не позволяет отлавливать категории, они создаются после его срабатывания
@receiver(m2m_changed, sender=Post.category.through)
def notify_subscribers_about_PostCreatedOrEdited(sender, instance, action, **kwargs):
    pass
    # sender - модель, которая активирует сигнал. в данном случае это модель  Post.
    # instance созданная/сохраняемая сущность модели Post
    # created - есть ли эта сущность на данный момент в БД.
    # Если сущность создается - отправляется одно, если изменяется, то отправляется другое
    # if action == 'post_add':
    #     subject = f'Создание поста: {instance.title} от автора {instance.author.name}'
    #     short_text = instance.text[0:150]
    #     categories = instance.category.all()
    #     for c in categories:
    #         # subscribers_mail = get_subscribers(c)
    #         # send_mail(
    #         #     subject=f'{subject} в категории {c}',
    #         #     message=short_text,
    #         #     from_email="kozhinova.olka@yandex.ru",
    #         #     recipient_list=subscribers_mail,
    #         # )
    # else:
    #     subject = f'Пост откорректирован: {instance.title} {instance.date.strftime("%d %m %Y")}'
