from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import MyCustomLoginView

urlpatterns = [
    path('login/', MyCustomLoginView.as_view(template_name = './login.html'), name='login'),
    path('logout/', 
         LogoutView.as_view(template_name = './logout.html'), 
         name='logout'),
   
#     path('signup/', 
#          BaseRegisterView.as_view(template_name = './signup.html'), 
#          name='signup'),
]
