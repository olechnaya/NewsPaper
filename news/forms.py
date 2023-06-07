from django import forms
from django.forms import ModelForm, Select, TextInput, BooleanField

from .models import Post, Category, Author

class PostForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    title = forms.CharField(
        label = 'Заголовок поста',
        widget = forms.TextInput(attrs={
            'placeholder': 'Здесь вводим заголовок...', 
            'class':'form-control',
            'id': 'adding-item-title'
        })
    )

    text = forms.CharField(
        label = 'Текст поста',
        widget = forms.Textarea(attrs={
            'placeholder': 'Здесь вводим текст поста...', 
            'class':'form-control',
            'rows': 3,
            'id': 'adding-item-text'
        })
    )

    author = forms.ModelChoiceField(
        label = 'Выбираем автора',
        queryset = Author.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select', 
            'id': 'adding-item-author'
        })
    )

    category = forms.ModelMultipleChoiceField(
        label = 'Выбираем категорию',
        queryset = Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
             
            'id': 'adding-item-category'
        })
    )

    postType = forms.ChoiceField(
        label = 'Выбираем тип поста',
        widget = forms.Select(attrs={
            'class': 'form-select', 
            'id': 'adding-item-type'
        }), 
        choices=Post.TYPE
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'author','category', 'postType']

#нифига пока не работает
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
