# Generated by Django 2.0.3 on 2018-05-06 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20180506_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movement',
            old_name='suply',
            new_name='supply',
        ),
    ]
