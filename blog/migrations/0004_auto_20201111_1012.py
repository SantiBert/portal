# Generated by Django 2.2.3 on 2020-11-11 13:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogentry_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
