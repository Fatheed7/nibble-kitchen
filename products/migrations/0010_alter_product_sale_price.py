# Generated by Django 4.0.5 on 2022-07-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_comments_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6),
            preserve_default=False,
        ),
    ]
