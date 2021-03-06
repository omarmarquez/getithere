# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 01:56
from __future__ import unicode_literals

import address.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_dt', models.DateField()),
                ('end_dt', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address1', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('address2', address.models.AddressField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='address.Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=False)),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('daily_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('address', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address1', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('address2', address.models.AddressField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='address.Address')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('image', models.ImageField(upload_to=b'')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Location'),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Owner'),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Customer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Item'),
        ),
    ]
