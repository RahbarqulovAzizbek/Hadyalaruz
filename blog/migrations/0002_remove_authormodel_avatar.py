# Generated by Django 4.0.5 on 2022-07-03 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authormodel',
            name='avatar',
        ),
    ]
