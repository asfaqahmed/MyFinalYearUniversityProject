# Generated by Django 2.2.14 on 2021-07-27 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_active',
        ),
    ]
