# Generated by Django 2.0.3 on 2018-05-06 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20180506_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suppliesmovement',
            name='cantidad',
        ),
    ]
