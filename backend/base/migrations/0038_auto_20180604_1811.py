# Generated by Django 2.0.5 on 2018-06-04 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_auto_20180603_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplies',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
