from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    required_css_class = 'required'
    error_css_class = 'error'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "" 

    first_name = forms.CharField(
        max_length=30,
        label = ('Имя'),
        required=False, 
        help_text='Optional.',
        widget=forms.TextInput(attrs={
            'placeholder': 'введите ваше имя...', 
            'class':'form-control',
            'id': 'adding-first-name' 
        }))
    
    last_name = forms.CharField(
        max_length=30,
        label = ('Фамилия'),
        required=False, 
        help_text='Optional.',
        widget=forms.TextInput(attrs={
            'placeholder': 'введите вашу фамилию...', 
            'class':'form-control',
            'id': 'adding-second-name' 
        }))
    email = forms.EmailField(
        label = ('Email'),
        widget=forms.TextInput(attrs={
            'placeholder': 'Email', 
            'class':'form-control',
            'id': 'adding-email' 
        }))
    username = forms.CharField(
        max_length=30,
        label = ('Имя пользователя'),
        widget=forms.TextInput(attrs={
            'placeholder': 'введите имя в системе...', 
            'class':'form-control',
            'id': 'adding-username' 
        }))
    password1 =  forms.CharField(
        max_length=30,
        label = ('Пароль'),
        widget=forms.PasswordInput(attrs={
            'placeholder': 'введите пароль...', 
            'class':'form-control',
            'id': 'adding-password1' 
        }))
    # TODO: сделать проверку полей
    password2 =  forms.CharField(
        max_length=30,
        label = ('Повторите пароль'),
        widget=forms.PasswordInput(attrs={
            'placeholder': 'повторите  пароль...', 
            'class':'form-control',
            'id': 'adding-password2' 
        }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    
    # def save(self, commit=True):
    #     user = super(SignupForm, self).save(commit=False)
    #     if commit:
    #         user.save()
    #     return user
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.save()
    # def signup(self, request, user):
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #     user.save()
    #     return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
