from django import forms
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm, LoginForm
from django.conf import settings 
from django.core.mail import send_mail

class CustomSignupForm(SignupForm):
    required_css_class = 'required'
    error_css_class = 'error'
  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "" 
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})

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
    # password =  forms.CharField(
    #     max_length=30,
    #     label = ('Пароль'),
    #     widget=forms.PasswordInput(attrs={
    #         'placeholder': 'введите пароль...', 
    #         'class':'form-control',
    #         'id': 'adding-password' 
    #     }))
    # password1 =  forms.CharField(
    #     max_length=30,
    #     label = ('Пароль'),
    #     widget=forms.PasswordInput(attrs={
    #         'placeholder': 'введите пароль...', 
    #         'class':'form-control',
    #         'id': 'adding-password1' 
    #     }))
    # # # TODO: сделать проверку полей
    # password2 =  forms.CharField(
    #     max_length=30,
    #     label = ('Повторите пароль'),
    #     widget=forms.PasswordInput(attrs={
    #         'placeholder': 'повторите  пароль...', 
    #         'class':'form-control',
    #         'id': 'adding-password2' 
    #     }))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        user.save()
        basic_group.user_set.add(user)
        return user


class MyLoginForm(LoginForm):
    required_css_class = 'required'
    error_css_class = 'error'

    password = forms.CharField(
        label = ('Пароль'),
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'id': 'password' 
        }))
    
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].label = 'Логин или почта'
        # self.fields['login'].help_text = 'Вы можете войти в систему, введя имя пользователя или почту'
        self.fields['login'].widget = forms.TextInput(attrs={
            'class':'form-control',
            'id': 'login' 
        })
    