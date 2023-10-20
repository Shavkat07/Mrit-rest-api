from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class TeamMember(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=30),
        about=models.CharField(max_length=200)
    )
    role = models.CharField(max_length=60)
    image = models.ImageField()
    telegram = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class ContactPage(TranslatableModel):
    translations = TranslatedFields(
        desciption=models.CharField(max_length=350)
    )
    full_name = models.CharField(max_length=66)
    email = models.EmailField()
    telegram = models.URLField()
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
