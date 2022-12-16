# Generated by Django 4.1.3 on 2022-12-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant_app", "0002_category_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]