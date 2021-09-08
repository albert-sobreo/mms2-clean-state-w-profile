# Generated by Django 3.2.3 on 2021-06-25 06:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_merchandiseinventory_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TempSCOtherFees',
            new_name='SCOtherFees',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='tempSCOtherFees',
        ),
        migrations.AddField(
            model_name='branch',
            name='SCOtherFees',
            field=models.ManyToManyField(blank=True, to='app.SCOtherFees'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='fullyReceived',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='qtyReceived',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='runningBalance',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='receivingreport',
            name='fullyReceived',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receivingreport',
            name='qtyReceived',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receivingreport',
            name='runningBalance',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='discountPercent',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='discountPeso',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='runningBalance',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='taxPeso',
            field=models.DecimalField(decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='taxRate',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='salescontract',
            name='taxType',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='salesContract',
            field=models.ManyToManyField(blank=True, to='app.SalesContract'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='scitemsMerch',
            field=models.ManyToManyField(blank=True, to='app.SCItemsMerch'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='taxPeso',
            field=models.DecimalField(decimal_places=5, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='receivingreport',
            name='taxPeso',
            field=models.DecimalField(decimal_places=5, max_digits=20, null=True),
        ),
    ]