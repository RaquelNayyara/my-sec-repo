# Generated by Django 4.2.5 on 2023-10-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
