# Generated by Django 3.2.3 on 2021-07-18 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0105_salesorder_voided'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='datetimeVoided',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='voidedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='soVoidedBy', to=settings.AUTH_USER_MODEL),
        ),
    ]