# Generated by Django 4.1.5 on 2023-01-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_alter_brand_name_alter_category_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="is_digital",
            field=models.BooleanField(default=False),
        ),
    ]
