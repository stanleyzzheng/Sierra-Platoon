# Generated by Django 4.1.3 on 2022-12-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]