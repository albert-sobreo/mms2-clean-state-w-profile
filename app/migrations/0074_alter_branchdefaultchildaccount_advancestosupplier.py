# Generated by Django 3.2.3 on 2021-06-30 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_branchdefaultchildaccount_branchprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchdefaultchildaccount',
            name='advancesToSupplier',
            field=models.ManyToManyField(blank=True, related_name='branchadvancestosupplier', to='app.AccountChild'),
        ),
    ]
