# Generated by Django 2.0.3 on 2018-04-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20180420_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='repuestos',
            field=models.ManyToManyField(related_name='repuestosauto', through='base.Autoparte', to='base.Repuesto'),
        ),
    ]
