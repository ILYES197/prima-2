# Generated by Django 5.0.4 on 2024-05-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Bidon', 'Bidon'), ('Balai', 'Balai'), ('Raclette', 'Raclette'), ('Chiffon', 'Chiffon'), ('textile', 'Textile'), ('liquide', 'Liquide'), ('brosse', 'Brosse'), ('manche', 'Manche')], max_length=50),
        ),
    ]
