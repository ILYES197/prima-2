# Generated by Django 5.0.4 on 2024-05-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
