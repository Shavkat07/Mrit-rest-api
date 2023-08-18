from django.db import models


class BlogCategory(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT)
    title = models.CharField(max_length=120)
    image = models.ImageField()
    text = models.TextField(max_length=5000)
    created = models.DateField(auto_now_add=True)
    watches = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
