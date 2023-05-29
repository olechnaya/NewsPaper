from django.urls import path
from .views import PostsList,PostDetail, PostCreateView, PostUpdateView, PostDeleteView, PostSearch # импортируем наше представление
 
 
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', PostsList.as_view(), name="posts"), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostDetail.as_view(), name="detail"),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('create/', PostCreateView.as_view(), name='create'), # localhost/posts/create/
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'), 
    path('search/', PostSearch.as_view(), name='search'),
]