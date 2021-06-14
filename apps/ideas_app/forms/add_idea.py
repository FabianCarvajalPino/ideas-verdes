from django.forms import ModelForm, widgets
from django import forms
from ..models import Idea

class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ['idea']
        widgets = {
            'idea':forms.TextInput(
                attrs={
                    'class': 'form-control form-wrapper',
                    'placeholder': "Cuantale a todos tu idea!",
                    'style': 'width:89%; margin:auto;',
                }
            )
        }
        labels = {
            'idea':''
        }