# Generated by Django 3.2.9 on 2021-12-15 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]