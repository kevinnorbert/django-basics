# Generated by Django 3.2.5 on 2021-08-16 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210816_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderline',
            old_name='product_code',
            new_name='code',
        ),
    ]