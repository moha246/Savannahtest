# Generated by Django 3.2.9 on 2021-11-29 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('innovations', '0002_auto_20211129_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
    ]
