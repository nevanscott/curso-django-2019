# Generated by Django 2.1 on 2018-08-11 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_auto_20180804_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(default='lesson', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reading',
            name='slug',
            field=models.SlugField(default='reading', unique=True),
            preserve_default=False,
        ),
    ]
