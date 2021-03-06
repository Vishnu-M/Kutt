# Generated by Django 2.0.4 on 2018-05-11 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shortify', '0009_userurl_page_icon_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserURLStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_clicked', models.DateTimeField()),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortify.UserURL')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
