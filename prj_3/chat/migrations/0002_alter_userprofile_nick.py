# Generated by Django 3.2.25 on 2024-11-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nick',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
