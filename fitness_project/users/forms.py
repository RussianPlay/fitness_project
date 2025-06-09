from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



def validate_password_strength(s):
    return True



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя пользователя',
        }),
        help_text='',
    )
    
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Электронная почта',
        }),
    )
    
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'autocomplete': 'new-password',
        }),
        strip=False,
        help_text='',
        validators=[validate_password_strength],
    )
    
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтверждение пароля',
            'autocomplete': 'new-password',
        }),
        strip=False,
        help_text='',
        validators=[validate_password_strength]
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже зарегистрирован.")
        return email



# class UserRegisterForm(UserCreationForm):
#     username = forms.CharField(
#         label='',
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Имя пользователя',
#         }),
#         help_text=''  # Убираем подсказку по умолчанию
#     )
    
#     email = forms.EmailField(
#         label='',
#         widget=forms.EmailInput(attrs={
#             'placeholder': 'Электронная почта',
#         })
#     )
    
#     password1 = forms.CharField(
#         label='',
#         widget=forms.PasswordInput(attrs={
#             'placeholder': 'Пароль',
#             'autocomplete': 'new-password'
#         }),
#         strip=False,
#         help_text=''  # Убираем подсказки о требованиях к паролю
#     )
    
#     password2 = forms.CharField(
#         label='',
#         widget=forms.PasswordInput(attrs={
#             'placeholder': 'Подтверждение пароля',
#             'autocomplete': 'new-password'
#         }),
#         strip=False,
#         help_text=''
#     )

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

















