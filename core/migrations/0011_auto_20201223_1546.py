# Generated by Django 2.2.3 on 2020-12-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201125_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='no-profile-picture.jpg', null=True, upload_to='profile/'),
        ),
    ]
