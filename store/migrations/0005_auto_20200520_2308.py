# Generated by Django 3.0.2 on 2020-05-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]