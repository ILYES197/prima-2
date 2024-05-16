# Generated by Django 5.0.4 on 2024-04-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_brandname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imageUrl',
            field=models.URLField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='totalReviewCount',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]