from django import forms
from .models import User

class checkout(forms.ModelForm):
    class Meta:
        model=User
        fields=('firstname','lastname','address1','address2','email','phonenumber')

