# Generated by Django 3.0.8 on 2020-08-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_shipping_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
