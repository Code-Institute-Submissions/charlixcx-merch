# Generated by Django 3.2 on 2022-03-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0004_rename_name_category_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='merch',
            name='product_hidden',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]