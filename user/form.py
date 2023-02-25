from django import forms
from .models import Menu
from django.contrib.auth.models import User

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('name', 'image', 'details', 'price')