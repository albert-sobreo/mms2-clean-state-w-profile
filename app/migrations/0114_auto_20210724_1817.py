# Generated by Django 3.2.3 on 2021-07-24 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0113_auto_20210724_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='receivingreport',
            name='datetimeVoided',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='receivingreport',
            name='voided',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='receivingreport',
            name='voidedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rrVoidedBy', to=settings.AUTH_USER_MODEL),
        ),
    ]
