# Generated by Django 2.0.3 on 2018-04-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20180420_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='repuestos',
        ),
        migrations.RemoveField(
            model_name='repuesto',
            name='auto_nombre',
        ),
        migrations.AddField(
            model_name='repuesto',
            name='autos',
            field=models.ManyToManyField(related_name='repu', through='base.Autoparte', to='base.Auto'),
        ),
    ]
