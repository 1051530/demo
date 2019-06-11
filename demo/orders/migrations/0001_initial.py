# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('姓', models.CharField(max_length=50)),
                ('名', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('地址', models.CharField(max_length=250)),
                ('郵遞區號', models.CharField(max_length=20)),
                ('城市', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=0)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(related_name='order_items', to='shop.Product')),
            ],
        ),
    ]
