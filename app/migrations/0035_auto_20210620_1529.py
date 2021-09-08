# Generated by Django 3.2.3 on 2021-06-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20210620_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequest',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='dateNeeded',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='department',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='intendedFor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
