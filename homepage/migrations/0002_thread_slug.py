# Generated by Django 4.2.16 on 2024-12-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.SlugField(default='default', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
