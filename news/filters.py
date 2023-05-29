import django_filters as filters # импортируем filterset, чем-то напоминающий знакомые дженерики
from django import forms
from .models import Post, Author

# создаём фильтр
class PostFilter(filters.FilterSet):
   
    title = filters.CharFilter(
        label='Заголовок', 
        lookup_expr='icontains',
        widget = forms.TextInput(attrs={
            'placeholder': 'Заголовок статьи для поиска', 
            'class':'form-control',        
        }))
    dateCreation = filters.CharFilter(
        label='Дата создания', 
        lookup_expr='gt',
        widget = forms.TextInput(attrs={
            'placeholder': 'YYYY-MM-DD HH:MM', 
            'class':'form-control',
        }))
    author = filters.ModelChoiceFilter(
        label = 'Автор',
        queryset = Author.objects.all())

    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т.е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = ('author', 'title', 'dateCreation')
        
        #('author', 'title', 'dateCreation') # поля, которые мы будем фильтровать (т.е. отбирать по каким-то критериям, имена берутся из моделей)