# Generated by Django 4.1 on 2022-08-03 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budjetapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Budget',
        ),
    ]