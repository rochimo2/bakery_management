# Generated by Django 2.0.3 on 2018-04-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='repuestos',
            field=models.ManyToManyField(related_name='nombrerepu', through='base.Autoparte', to='base.Repuesto'),
        ),
    ]
