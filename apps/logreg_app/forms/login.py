from django.forms import ModelForm, PasswordInput
from django import forms
from ..models import User

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:70%'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'width:70%'}), required=True)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = User.authenticate(email, password)
        if not user:
            raise forms.ValidationError('Usuario y/o contraseña incorrecta')
        return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data['password']
        user = User.authenticate(email, password)
        return user