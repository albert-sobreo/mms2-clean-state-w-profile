# Generated by Django 3.2.3 on 2021-07-31 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0123_auto_20210731_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='POItemsOther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('remaining', models.IntegerField()),
                ('qty', models.PositiveIntegerField()),
                ('purchasingPrice', models.DecimalField(decimal_places=5, max_digits=20)),
                ('totalPrice', models.DecimalField(decimal_places=5, max_digits=20)),
                ('delivered', models.BooleanField(default=False, null=True)),
                ('qtyReceived', models.IntegerField(default=0)),
                ('otherInventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='poitemsother', to='app.otherinventory')),
                ('purchaseOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='poitemsother', to='app.purchaseorder')),
            ],
        ),
    ]
