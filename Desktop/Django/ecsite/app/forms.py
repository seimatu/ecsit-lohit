from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=('email',)


from django import forms

class AddToCartForm(forms.Form):
    num=forms.IntegerField(
        label='quantity',
        min_value=1,
        required=True,
        )

class PurchaseForm(forms.Form):
    zip_code=forms.CharField(
        label='郵便番号',
        max_length=7,
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'数字７桁(ハイフンなし)'}))
    address=forms.CharField(
        label='住所',
        max_length=100,
        required=False
    )