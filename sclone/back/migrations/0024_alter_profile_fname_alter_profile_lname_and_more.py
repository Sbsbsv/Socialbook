# Generated by Django 4.1.3 on 2023-01-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0023_alter_profile_fname_alter_profile_lname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fname',
            field=models.CharField(default='Mr./Mrs.', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lname',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]