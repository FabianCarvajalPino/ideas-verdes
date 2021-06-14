from django.forms import ModelForm, PasswordInput
from django import forms
from ..models import User

class RegisterForm(ModelForm):

    password = forms.CharField(widget = PasswordInput(attrs={
        "value": "",
        'placeholder': "Min. 8 caracteres",
        "class":"form-control",
        "style":"width: 70%; "
    }))
    confirm_password = forms.CharField(widget = PasswordInput(attrs={
        'placeholder': "Min. 8 caracteres",
        "class":"form-control",
        "style":"width: 70%;"
    }))

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(
                attrs={
                    "class":"form-control test-class",
                    "placeholder": "Solo letras, min 2 car.",
                    "style": "width: 70%;"
                }
            ),
            'alias':forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Solo letras, min 2 car.",
                    "style": "width: 70%;"
                }
            ),
            'email': forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Ej: nombre@dominio.algo",
                    "style":"width: 70%;"
                }
            )
        }

        labels = {
            'name': 'Nombre completo',
            'alias': 'Alias',
            'email': "Email",
            'password': 'Contraseña',
            'confirm_password': 'Confirmar contraseña'
        }

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pw = cleaned_data.get('password')
        confirm_pw = cleaned_data.get('confirm_password')
        if pw != confirm_pw:
            raise forms.ValidationError(
                "Las contraseñas no coinciden"
            )