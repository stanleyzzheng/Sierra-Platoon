# Generated by Django 3.2.4 on 2022-11-09 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodDelivery', '0009_auto_20221109_0237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditem',
            old_name='order',
            new_name='orders',
        ),
    ]