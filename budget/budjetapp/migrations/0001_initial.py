# Generated by Django 4.1 on 2022-08-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coming_or_spending', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('money', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
