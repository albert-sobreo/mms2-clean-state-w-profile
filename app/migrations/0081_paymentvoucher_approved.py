# Generated by Django 3.2.3 on 2021-07-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0080_auto_20210705_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentvoucher',
            name='approved',
            field=models.BooleanField(blank=True, default='False', null=True),
        ),
    ]
