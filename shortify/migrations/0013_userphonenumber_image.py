# Generated by Django 2.0.4 on 2018-05-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortify', '0012_auto_20180520_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='userphonenumber',
            name='image',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
    ]