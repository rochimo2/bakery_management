# Generated by Django 2.0.5 on 2018-06-06 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_auto_20180606_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='horas_trabajadas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]