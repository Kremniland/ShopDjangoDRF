# Generated by Django 4.1.5 on 2023-01-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='manufacturer', to='shop.product'),
        ),
    ]
