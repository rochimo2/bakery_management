# Generated by Django 2.0.3 on 2018-05-14 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_auto_20180510_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ingredientes',
            field=models.ManyToManyField(related_name='pepe', through='base.Supplies', to='base.Supply'),
        ),
    ]
