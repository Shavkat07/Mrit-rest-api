from django.db import models
from ckeditor.fields import RichTextField


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=70)


class Portfolio(models.Model):
    category = models.ForeignKey(PortfolioCategory, on_delete=models.PROTECT)
    title = models.CharField(max_length=70)
    image = models.ImageField()
    link = models.URLField()
    textfull = RichTextField()
    watches = models.PositiveBigIntegerField(default=0)
    like = models.PositiveBigIntegerField(default=0)


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.PROTECT)
    image = models.ImageField()
