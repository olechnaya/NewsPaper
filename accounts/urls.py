from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import  MyCustomLoginView, upgrade_me, downgrade_me

urlpatterns = [
    path('login/', MyCustomLoginView.as_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = './logout.html'),name='logout'),   
#     path('signup/', 
#          BaseRegisterView.as_view(template_name = 'signup.html'), # так и не поняла почему здесь можно обойтись без ./
#          name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
    path('downgrade/', downgrade_me, name = 'downgrade')
]
