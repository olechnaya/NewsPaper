from django.urls import path
from .views import (
    AuthorList,
    PostList,
    PostDetail,
    PostCreateView,
    PostUpdateView,  # вьюхи yuryatlant
    PostDeleteView,
    PostSearch,
    NewsCategoryView,
    СategoryCreateView,
    CategoryDetailView,
    UnsubscribeCategory,
    SubscribeCategory,
    some_page)  # импортируем наше представление

app_name = "news"

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам 
    # у нас останется пустым, позже станет ясно почему
    path('', PostList.as_view(), name="posts"),  # т.к. сам по себе это класс,
                                                 # то нам надо представить этот класс в виде view. 
                                                 # Для этого вызываем метод as_view
                                                 # добавим кэширование на детали товара. 
                                                 # Раз в 10 минут товар будет записываться 
                                                 # в кэш для экономии ресурсов
    path('posts/<int:pk>', 
         PostDetail.as_view(), 
         name="post"),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('posts/create/', 
         PostCreateView.as_view(), 
         name='create'),  # localhost/posts/create/
    path('category/create/',
         СategoryCreateView.as_view(),
         name='create_category'),
    
    path('category/<int:pk>/',
         CategoryDetailView,
         name='category'),
    path('categories/subscribe/<int:pk>',
         SubscribeCategory,
         name='category_subscribe'),
    path('categories/unsubscribe/<int:pk>',
         UnsubscribeCategory,
         name='category_unsubscribe'),
    #path('categories/<str:cat_name>', CategoryDetailView, name='category'), 
    # здесь мы хотим имя категории, не цифру, поэтому str, после двоеточия - всё что угодно, как, что во вьюхе обзовём

    path('categories/',
         NewsCategoryView.as_view(),
         name='categories'),
    path('posts/update/<int:pk>',
         PostUpdateView.as_view(),
         name='update'),
    path('posts/delete/<int:pk>',
         PostDeleteView.as_view(),
         name='delete'),
    path('posts/search/',
         PostSearch.as_view(),
         name='search'),
    path('authors/',
         AuthorList.as_view(),
         name="authors"),
    path('some_page/<int:question_id>',
         some_page,
         name="some_page"),
]
