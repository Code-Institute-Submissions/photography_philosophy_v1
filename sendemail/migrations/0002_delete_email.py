# Generated by Django 3.0.8 on 2020-08-31 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendemail', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
    ]