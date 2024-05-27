from django import forms

from .models import User, HotelsComment


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "age", "sex"]