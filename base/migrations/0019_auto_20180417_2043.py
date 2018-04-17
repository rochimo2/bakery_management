# Generated by Django 2.0.3 on 2018-04-17 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_product_supply'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('feature1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='supply',
        ),
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.ManyToManyField(through='base.ProductFeature', to='base.Feature'),
        ),
        migrations.AddField(
            model_name='productsupply',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Product'),
        ),
        migrations.AddField(
            model_name='productsupply',
            name='supply1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Supply'),
        ),
        migrations.AddField(
            model_name='productfeature',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplies',
            field=models.ManyToManyField(through='base.ProductSupply', to='base.Supply'),
        ),
    ]
