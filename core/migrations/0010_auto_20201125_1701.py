# Generated by Django 2.2.3 on 2020-11-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_friendsites'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendsites',
            name='site_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='sitio'),
        ),
        migrations.AlterField(
            model_name='friendsites',
            name='image_ref',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='friendsites/'),
        ),
    ]
