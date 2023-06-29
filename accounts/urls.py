from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import MyCustomLoginView, upgrade_me

urlpatterns = [
    path('login/', MyCustomLoginView.as_view(template_name = './login.html'), 
         name='login'),
    path('logout/', 
         LogoutView.as_view(template_name = './logout.html'), 
         name='logout'),   
#     path('signup/', 
#          BaseRegisterView.as_view(template_name = 'signup.html'), # так и не поняла почему здесь можно обойтись без ./
#          name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade')
]
