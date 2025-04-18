# Generated by Django 5.1.7 on 2025-03-15 11:10

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('detail_description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('categories', models.ManyToManyField(to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
