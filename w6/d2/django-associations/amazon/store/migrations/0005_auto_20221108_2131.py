# Generated by Django 3.2.4 on 2022-11-09 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20221108_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.shop'),
        ),
    ]
