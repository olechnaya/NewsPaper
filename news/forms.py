from django import forms
from django.forms import ModelForm

from .models import Post, Category, Author

choices = Category.objects.all().values_list('name','name')

class PostForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    # title = forms.CharField(
    #     label = 'Заголовок поста',
    #     widget = forms.TextInput(attrs={
    #         'placeholder': 'Здесь вводим заголовок...', 
    #         'class':'form-control',
    #         'id': 'adding-item-title'
    #     })
    # )

    # text = forms.CharField(
    #     label = 'Текст поста',
    #     widget = forms.Textarea(attrs={
    #         'placeholder': 'Здесь вводим текст поста...', 
    #         'class':'form-control',
    #         'rows': 3,
    #         'id': 'adding-item-text'
    #     })
    # )

    # author = forms.ModelChoiceField(
    #     label = 'Выбираем автора',
    #     queryset = Author.objects.all(),
    #     widget=forms.Select(attrs={
    #         'class': 'form-select', 
    #         'id': 'adding-item-author'
    #     })
    # )

    # category = forms.ModelMultipleChoiceField(
    #     label = 'Выбираем категорию',
    #     # queryset = Category.objects.all(),
    #     choices = choices,
    #     widget=forms.CheckboxSelectMultiple(attrs={
             
    #         'id': 'adding-item-category'
    #     })
    # )

    # postType = forms.ChoiceField(
    #     label = 'Выбираем тип поста',
    #     widget = forms.Select(attrs={
    #         'class': 'form-select', 
    #         'id': 'adding-item-type'
    #     }), 
    #     choices=Post.TYPE
    # )

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