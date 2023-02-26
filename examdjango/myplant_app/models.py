from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.db import models


def validate_capitalized(value):
    if not value[0].isupper():
        raise ValueError("Your name must start with a capital letter!")


def plant_name_validator(value):
    for x in value:
        if not x.isalpha():
            raise ValidationError("Plant name should contain only letters!")


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    first_name = models.CharField(verbose_name="First Name", max_length=20, validators=[validate_capitalized])
    last_name = models.CharField(verbose_name="Last Name", max_length=20, validators=[validate_capitalized])
    profile_picture = models.URLField(verbose_name="Profile Picture", null=True, blank=True)


class Plant(models.Model):
    TYPES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )

    type = models.CharField(verbose_name="Type", max_length=14, choices=TYPES)
    name = models.CharField(verbose_name="Name", validators=[MinLengthValidator(2), plant_name_validator], max_length=20)
    image_url = models.URLField(verbose_name="Image URL")
    description = models.TextField(verbose_name="Description")
    price = models.FloatField(verbose_name="Price")