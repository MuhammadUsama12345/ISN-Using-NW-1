# Generated by Django 2.2.24 on 2021-06-27 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isenw_app', '0017_auto_20210627_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='image',
        ),
    ]
