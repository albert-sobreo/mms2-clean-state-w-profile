# Generated by Django 3.2.3 on 2021-06-19 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_remove_purchaserequest_journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorQuotesMerch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchInventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vendorquotesmerch', to='app.merchandiseinventory')),
                ('purchaseRequest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vendorquotesmerch', to='app.purchaserequest')),
            ],
        ),
        migrations.CreateModel(
            name='VendorQuotesItemsMerch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=5, max_digits=18)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vendorquotesitemsmerch', to='app.party')),
            ],
        ),
    ]
