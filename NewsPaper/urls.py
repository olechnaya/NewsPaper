from django.contrib import admin
from django.urls import path, include
import news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('accounts/', include('accounts.urls')), #logout, upgrade тут сидят - они нужны
    path('oauth/', include('allauth.urls'), name="account_login" )    
]
