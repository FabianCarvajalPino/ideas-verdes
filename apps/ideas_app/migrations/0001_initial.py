# Generated by Django 2.2.4 on 2021-06-12 01:03

import apps.ideas_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logreg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.TextField(validators=[apps.ideas_app.models.validar_strings])),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(related_name='ideas_liked', to='logreg_app.User')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to='logreg_app.User')),
            ],
        ),
    ]
