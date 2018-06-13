# Generated by Django 2.0.3 on 2018-05-10 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_auto_20180510_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha de la operación')),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de venta')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cliente', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.Client')),
                ('orden', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.Order')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SuppliesPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Purchase')),
                ('supply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Supply')),
            ],
        ),
        migrations.RemoveField(
            model_name='movement',
            name='client',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='orden',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='suplier',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='supply',
        ),
        migrations.RemoveField(
            model_name='suppliesmovement',
            name='movement',
        ),
        migrations.RemoveField(
            model_name='suppliesmovement',
            name='supply',
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='movement',
        ),
        migrations.DeleteModel(
            name='Movement',
        ),
        migrations.DeleteModel(
            name='SuppliesMovement',
        ),
        migrations.AddField(
            model_name='purchase',
            name='suplier',
            field=models.ManyToManyField(related_name='supliers', through='base.Suppliers', to='base.Supplier'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='supply',
            field=models.ManyToManyField(related_name='suplies', through='base.SuppliesPurchase', to='base.Supply'),
        ),
        migrations.AddField(
            model_name='suppliers',
            name='purchase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Purchase'),
        ),
    ]
