from django import forms
from django.forms import ModelForm

from .models import Post, Category, Author

choices = Category.objects.all().values_list('name','name')

class PostForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
 
    class Meta:
        model = Post
        fields = ['title', 'text', 'author','category', 'postType']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-select'}),
            'category': forms.CheckboxSelectMultiple(choices=choices),
            'postType': forms.Select(choices=Post.TYPE, attrs={'class':'form-select'}),
        }
       
        labels = {
            'title' : 'Заголовок поста',
            'text' : 'Текст поста',
            'author': 'Выбираем автора',
            'category': 'Выбираем категорию',
            'postType': 'Выбираем тип'
        }