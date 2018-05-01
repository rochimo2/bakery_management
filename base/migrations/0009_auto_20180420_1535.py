# Generated by Django 2.0.3 on 2018-04-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20180420_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repuesto',
            name='autos',
        ),
        migrations.AddField(
            model_name='auto',
            name='repuestos',
            field=models.ManyToManyField(related_name='autos', through='base.Autoparte', to='base.Repuesto'),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='auto_nombre',
            field=models.CharField(default='', max_length=80),
        ),
    ]
