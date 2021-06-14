from django.db import models
from django.core.exceptions import ValidationError
from django.core import validators
import re
import bcrypt


# Create your models here.

def validar_strings(string):
    #validar el largo minimo
    if len(string) < 2:
        raise ValidationError(
            f'{string} no coincide con los requisitos, ese campo debiese tener al menos 2 caracteres'
        )
    #validar que solo se ingresen letras
    NAME_REGEX = re.compile(r'^[a-zA-Z\s]+$')
    if not NAME_REGEX.match(string):
        raise ValidationError(
            f'{string} no coincide con los requisitos, porfavor ingresar solo letras'
        )

def validar_longitud_pw(pw):
    #validar longitud minima en contraseña
    if len(pw) < 8:
        raise ValidationError(
            'La contraseña debiese tener al menos 8 caracteres'
        )

def validar_email(email):
    #validar la estructura de un email
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(email):
        raise ValidationError(
            f'{email} no cumple el formato requerido, intenta con nombre@dominio.algo'
        )
    for user in User.objects.all():
        if email.lower() == user.email.lower():
            raise ValidationError(
                f'El email {email} ya existe, intenta con otro'
            )

class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, validators=[validar_strings])
    alias = models.CharField(max_length=100, blank=False, null=False, validators=[validar_strings])
    email = models.CharField(max_length=255, blank=False, null=False, validators=[validar_email])
    password = models.CharField(max_length=60, blank=False, null=False, validators=[validar_longitud_pw])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def authenticate(email, password):
        user = User.objects.filter(email = email)[0]
        if user:
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return user
        return None