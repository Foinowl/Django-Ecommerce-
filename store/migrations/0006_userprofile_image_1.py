# Generated by Django 3.0.2 on 2020-05-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200520_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image_1',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
