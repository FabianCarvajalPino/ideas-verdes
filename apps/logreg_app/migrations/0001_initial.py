# Generated by Django 2.2.4 on 2021-06-10 19:39

import apps.logreg_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[apps.logreg_app.models.validar_strings])),
                ('alias', models.CharField(max_length=100, validators=[apps.logreg_app.models.validar_strings])),
                ('email', models.CharField(max_length=255, validators=[apps.logreg_app.models.validar_email])),
                ('password', models.CharField(max_length=60, validators=[apps.logreg_app.models.validar_longitud_pw])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
