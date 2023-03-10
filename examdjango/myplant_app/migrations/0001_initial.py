# Generated by Django 3.2.16 on 2022-12-21 09:14

import django.core.validators
from django.db import migrations, models
import examdjango.myplant_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Plant name should contain only letters!')])),
                ('image_url', models.URLField(verbose_name='Image URL:')),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[examdjango.myplant_app.models.validate_capitalized])),
                ('last_name', models.CharField(max_length=20, validators=[examdjango.myplant_app.models.validate_capitalized])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
