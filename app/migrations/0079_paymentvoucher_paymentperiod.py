# Generated by Django 3.2.3 on 2021-07-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0078_auto_20210705_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentvoucher',
            name='paymentPeriod',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
