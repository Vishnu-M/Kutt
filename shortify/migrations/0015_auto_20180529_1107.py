# Generated by Django 2.0.4 on 2018-05-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortify', '0014_auto_20180526_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphonenumber',
            name='image',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
    ]
