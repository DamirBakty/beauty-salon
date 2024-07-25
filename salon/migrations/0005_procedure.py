# Generated by Django 5.0.7 on 2024-07-25 09:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0004_salon_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название процедуры')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('master', models.ManyToManyField(related_name='procedures', to='salon.master')),
                ('salon', models.ManyToManyField(related_name='procedures', to='salon.salon')),
            ],
        ),
    ]
