from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def get_subscribers(category):
    user_email=[]
    for user in category.subscribers.all():
        user_email.append(user.email)
    return user_email

# Задача - уведомление о добавлении новости в подписках

def new_post_subscription_notification(instance):    
    template ='mailing/new_post_notification.html'
    subject = f'Создание поста: {instance.title} от автора {instance.author.name}'

    for category in instance.category.all():
        email_subject = subject
        email_users = get_subscribers(category)
        html = render_to_string(
            template_name = template,
            context = {
                'category': category,
                'post' : instance,
                },
            )
        msg = EmailMultiAlternatives(
            subject = email_subject,
            body = '',
            from_email = settings.DEFAULT_FROM_EMAIL,
            to = email_users,
            )
        msg.attach_alternative(html, "text/html")
        msg.send()
