from django import forms

from .models import User, HotelsComment


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "age", "sex"]
        error_messages = {
            'age': {
                'invalid': "Age must be more than 18 or less than 90.",
            },
        }

class HotelsCommentForm(forms.ModelForm):
    class Meta:
        model = HotelsComment
        fields = ["persons", "hotels","comment", "hotel_rating"]
        widgets = {
            "comment": forms.Textarea(attrs={"size": 500, 'class': 'special', "required": False})
        }