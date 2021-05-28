# from .models import PetModel
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from PETApp.models import PetModel


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PetRegisterForm(forms.ModelForm):
    class Meta:
        model = PetModel
        fields = ['owner', 'petName', 'petImage', 'type', 'category', 'amount']
