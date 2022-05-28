from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppTuitlon.models import Avatar
from AppTuitlon.models import Tuitl

class TuitlForm(forms.Form):

    contenido = forms.CharField(max_length=200)
    imagen = forms.ImageField()

class TuitlForm2(forms.ModelForm):

    class Meta:

        model = Tuitl
        fields = ['contenido', 'imagen']

class RegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 


class AvatarForm(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ['user', 'imagen']