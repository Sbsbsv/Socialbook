# Generated by Django 4.1 on 2022-08-07 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0007_profile_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='text',
        ),
    ]