from django import forms


class RegistrarionForm(forms.Form):
    email = forms.EmailField(label='Your ass')

