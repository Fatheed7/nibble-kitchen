# Generated by Django 4.0.5 on 2022-06-26 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footer_content', '0002_postage_name_privacy_name_refunds_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Refunds',
            new_name='Returns',
        ),
    ]
