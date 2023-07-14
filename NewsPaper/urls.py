from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('user/', include('user.urls')),
    path('accounts/', include('accounts.urls')), #logout, upgrade тут сидят - они нужны
    path('oauth/', include('allauth.urls'), name="account_login" ),   
]

handler404 = 'news.views.error_404'
handler403 = 'news.views.error_403'