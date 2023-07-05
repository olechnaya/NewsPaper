from django.contrib import admin
from django.urls import path, include
import news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('user/', include('user.urls')),
]

handler404 = 'news.views.error_404'
handler403 = 'news.views.error_403'