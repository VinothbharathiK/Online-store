# Generated by Django 5.1.7 on 2025-04-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_product_ram'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='camera',
            field=models.CharField(blank=True, default='50MP + 10MP+ 2MP Camera', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='display',
            field=models.CharField(blank=True, default='6.8" Dynamic AMOLED 2X, 70HZ', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.DecimalField(blank=True, decimal_places=0, default=4, max_digits=3),
        ),
    ]
