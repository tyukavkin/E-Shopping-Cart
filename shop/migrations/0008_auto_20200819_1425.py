# Generated by Django 3.1 on 2020-08-19 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
