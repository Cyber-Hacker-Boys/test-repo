from django import forms

from .models import Master


class RegistrarionForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['email']
