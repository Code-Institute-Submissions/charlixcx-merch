# Generated by Django 3.2 on 2022-03-23 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0003_merch_limited_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='product_name',
        ),
    ]