# Generated by Django 4.2.4 on 2023-08-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='role',
            field=models.CharField(max_length=60, verbose_name='testing'),
        ),
    ]
