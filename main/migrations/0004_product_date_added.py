# Generated by Django 4.2.5 on 2023-10-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateField(auto_now_add=True, default='2023-10-04'),
            preserve_default=False,
        ),
    ]