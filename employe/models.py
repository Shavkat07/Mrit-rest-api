from django.db import models
from django.utils.translation import gettext as _
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

    # def __str__(self):
    #     return self.name