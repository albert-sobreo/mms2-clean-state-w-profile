# Generated by Django 3.2.3 on 2021-06-26 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_alter_purchaseorder_fullyreceived'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='rred',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='poed',
            field=models.BooleanField(default=False),
        ),
    ]