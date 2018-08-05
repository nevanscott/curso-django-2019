# Generated by Django 2.1 on 2018-08-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_auto_20180804_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reading',
            name='lessons',
        ),
        migrations.AddField(
            model_name='lesson',
            name='readings',
            field=models.ManyToManyField(to='curriculum.Reading'),
        ),
    ]