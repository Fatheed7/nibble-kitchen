# Generated by Django 4.0.5 on 2022-06-26 22:53

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django_quill.fields.QuillField()),
            ],
            options={
                'verbose_name_plural': 'Postage and Packaging',
            },
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django_quill.fields.QuillField()),
            ],
            options={
                'verbose_name_plural': 'Privacy Policy',
            },
        ),
        migrations.CreateModel(
            name='Refunds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', django_quill.fields.QuillField()),
            ],
            options={
                'verbose_name_plural': 'Refunds & Returns',
            },
        ),
    ]
