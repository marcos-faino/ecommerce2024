from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class CadUsuarioForm(UserCreationForm):

    captcha = CaptchaField(label="Digite o que aparece na imagem:")
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username',
                  'password1', 'password2', 'captcha']
