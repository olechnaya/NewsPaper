from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from django import forms

class BaseRegisterForm(UserCreationForm):
    error_css_class = 'error'
    required_css_class = 'required'

    username = forms.CharField(
        label = "Имя пользователя",
        widget=forms.TextInput(attrs={
            # 'placeholder': 'введите имя для использования в системе', 
            'class':'form-control',
            'id': 'user-login-name' 
        }))
    email = forms.EmailField(
        label = "Email",
        widget=forms.TextInput(attrs={
            # 'placeholder': 'введите ваш email', 
            'class':'form-control',
            'id': 'user-email' 
        }))
    first_name = forms.CharField(
        label = "Имя",
        widget=forms.TextInput(attrs={
            # 'placeholder': 'введите ваше имя', 
            'class':'form-control',
            'id': 'user-first-name' 
        }))
    last_name = forms.CharField(
        label = "Фамилия",
        widget=forms.TextInput(attrs={
            # 'placeholder': 'введите вашу фамилию', 
            'class':'form-control',
            'id': 'user-second-name' 
        }))
    password1 = forms.CharField(
        label = "Пароль",
        widget= forms.PasswordInput(attrs={
            'class':'form-control',
            'id': 'user-password1' 
        }))
    
    my_custom_error_text = {
        'required': 'Поле обязательно для заполнения',
        'invalid': 'Введите корректное значение'
    }

    password2 = forms.CharField(
        label = "Подтверждение пароля",
        # help_text= 'Минимальная длина пароля 8 символов.',
        error_messages= my_custom_error_text,
        widget= forms.PasswordInput(attrs={
            'class':'form-control',
            'id': 'user-password2',
            
        })
    )

    def __init__(self, *args, **kwargs):
        super(BaseRegisterForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

        # for fieldname in ['username', 'password1', 'password2']:
        #     self.fields[fieldname].help_text = None


    class Meta:
        model = User
        fields = ("username", 
                  "first_name", 
                  "last_name", 
                  "email", 
                  "password1", 
                  "password2", )
    
    def save(self, commit=True):
        user = super(BaseRegisterForm, self).save(commit=False)
        basic_group = Group.objects.get(name='common')
        user.save()
        basic_group.user_set.add(user)
        return user
    
# olga - _Terrariem78