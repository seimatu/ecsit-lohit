from django import forms
from . models import AllInfo

class AllInfoForm(forms.ModelForm):
    class Meta:
        model=AllInfo
        fields=(
            'name',
            'age',
            'adress',
            'Email',
        )