# Generated by Django 2.0.3 on 2018-04-19 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Autoparte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Auto')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('dirección', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('tipo', models.CharField(max_length=70)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='$')),
                ('cantidad', models.IntegerField(null=True, verbose_name='cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de la operación')),
                ('tipo', models.CharField(choices=[('VT', 'Venta'), ('CP', 'Compra')], default='VT', max_length=2)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de pedido')),
                ('ocasion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('caracteristicas', models.ManyToManyField(through='base.Features', to='base.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=80)),
                ('auto_nombre', models.CharField(default='', max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('dirección', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('contacto', models.CharField(blank=True, max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Supplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('marca', models.CharField(max_length=70)),
                ('tipo', models.CharField(max_length=70)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unidad', models.CharField(choices=[('KG', 'Kilo'), ('UN', 'Unidad'), ('LT', 'Litro'), ('MT', 'Metro')], default='KG', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='supplies',
            name='supply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Supply'),
        ),
        migrations.AddField(
            model_name='product',
            name='ingredientes',
            field=models.ManyToManyField(through='base.Supplies', to='base.Supply'),
        ),
        migrations.AddField(
            model_name='order',
            name='ingredientes_utilizados',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.Supply'),
        ),
        migrations.AddField(
            model_name='order',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Product'),
        ),
        migrations.AddField(
            model_name='movement',
            name='orden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Order'),
        ),
        migrations.AddField(
            model_name='movement',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Product'),
        ),
        migrations.AddField(
            model_name='movement',
            name='suplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Supplier'),
        ),
        migrations.AddField(
            model_name='movement',
            name='supply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Supply'),
        ),
        migrations.AddField(
            model_name='features',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Product'),
        ),
        migrations.AddField(
            model_name='client',
            name='pedido',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.Order'),
        ),
        migrations.AddField(
            model_name='autoparte',
            name='repuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Repuesto'),
        ),
        migrations.AddField(
            model_name='auto',
            name='repuestos',
            field=models.ManyToManyField(through='base.Autoparte', to='base.Repuesto'),
        ),
    ]
