# Generated by Django 5.0.7 on 2024-07-29 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0015_alter_servicecategory_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_category',
        ),
    ]