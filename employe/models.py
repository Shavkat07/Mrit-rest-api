from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=60, verbose_name="testing")
    about = models.CharField(max_length=200)
    image = models.ImageField()
    telegram = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name