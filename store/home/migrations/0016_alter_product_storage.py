# Generated by Django 5.1.7 on 2025-04-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_product_processor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=4),
        ),
    ]
