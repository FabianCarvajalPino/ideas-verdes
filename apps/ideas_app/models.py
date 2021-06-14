from django.db import models
from django.core.exceptions import ValidationError
from django.core import validators
from ..logreg_app.models import User
# Create your models here.

def validar_strings(string):
    #validar el largo minimo
    if len(string) < 1:
        raise ValidationError(
            'Este campo no puede estar vacío'
        )

class Idea(models.Model):
    owner = models.ForeignKey(User, related_name='ideas', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='ideas_liked')
    idea = models.TextField(blank=False, null=False, validators=[validar_strings])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)