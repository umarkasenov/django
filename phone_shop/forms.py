from django import forms
from . import models


class PhoneShopForm(forms.ModelForm):
    class Meta:
        model = models.PhoneShop
        fields = '__all__'
