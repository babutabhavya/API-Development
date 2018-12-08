# Generated by Django 2.1.3 on 2018-11-14 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assign_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlickrImagesByGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.CharField(max_length=25)),
                ('group_name', models.CharField(max_length=25)),
                ('image', models.CharField(max_length=255)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]