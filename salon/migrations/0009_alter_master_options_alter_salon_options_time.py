# Generated by Django 5.0.7 on 2024-07-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0008_remove_master_service_remove_salon_master_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='master',
            options={'verbose_name': 'мастер', 'verbose_name_plural': 'мастера'},
        ),
        migrations.AlterModelOptions(
            name='salon',
            options={'verbose_name': 'салон', 'verbose_name_plural': 'салоны'},
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Время')),
                ('available', models.BooleanField(default=True, verbose_name='Доступно')),
                ('master', models.ManyToManyField(blank=True, related_name='available_time', to='salon.master', verbose_name='Мастер')),
                ('salon', models.ManyToManyField(blank=True, related_name='available_time', to='salon.salon', verbose_name='Салон')),
            ],
        ),
    ]