# Generated by Django 3.2.3 on 2021-06-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0064_auto_20210628_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inwardinventory',
            name='amountTotal',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=18, null=True),
        ),
    ]
