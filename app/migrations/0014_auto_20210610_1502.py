# Generated by Django 3.1.7 on 2021-06-10 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210610_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='status',
            field=models.CharField(default='Available', max_length=50, null=True),
        ),
    ]
