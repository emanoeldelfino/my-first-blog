# Generated by Django 2.2.17 on 2020-12-27 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201226_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo_url',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='blog_photos/'),
        ),
    ]