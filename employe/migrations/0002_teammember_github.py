# Generated by Django 4.2.5 on 2023-10-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
