# Generated by Django 4.1.3 on 2022-12-14 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("market_app", "0002_item_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="categorry",
            new_name="category",
        ),
    ]