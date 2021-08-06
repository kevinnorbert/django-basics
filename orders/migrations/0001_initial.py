# Generated by Django 3.2.5 on 2021-08-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('order_no', models.CharField(max_length=50, unique=True)),
                ('grand_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_code', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('unit_price', models.FloatField()),
                ('tax_rate', models.FloatField()),
                ('order_id', models.BigIntegerField()),
            ],
        ),
    ]
