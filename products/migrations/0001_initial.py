# Generated by Django 3.2.9 on 2023-03-19 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=20, verbose_name='Kategoriya')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.CharField(max_length=10, verbose_name='Joyi')),
            ],
            options={
                'verbose_name_plural': 'Location',
            },
        ),
        migrations.CreateModel(
            name='MeasureType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_type', models.CharField(default='m', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Mahsulot nomi')),
                ('description', models.TextField(verbose_name='Izoh')),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Sotilish narxi ($)')),
                ('cost_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Tannarx ($)')),
                ('length', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Uzunligi (m)')),
                ('status', models.BooleanField(default=False)),
                ('barcode', models.CharField(default=0, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Qo'shgan odam")),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Kategoriya')),
                ('measure_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.measuretype', verbose_name="O'lchov birligi")),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.location', verbose_name='Joyi')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='product_images', verbose_name='Rasmi')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Mahsulot')),
            ],
        ),
    ]