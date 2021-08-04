# Generated by Django 3.2.5 on 2021-08-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
