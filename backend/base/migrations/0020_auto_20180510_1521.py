# Generated by Django 2.0.3 on 2018-05-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_auto_20180510_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='supply',
            field=models.ManyToManyField(blank=True, null=True, related_name='suplies', through='base.SuppliesMovement', to='base.Supply'),
        ),
    ]
