# Generated by Django 2.0.3 on 2018-04-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20180420_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='nombre',
            field=models.CharField(default='', max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='repuesto',
            name='nombre',
            field=models.CharField(default='', max_length=80, unique=True),
        ),
    ]
