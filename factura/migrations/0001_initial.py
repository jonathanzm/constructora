# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-10-01 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('cedula', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('cantidad', models.CharField(max_length=200)),
                ('descuento', models.CharField(max_length=200)),
                ('iva', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
            ],
        ),
    ]
