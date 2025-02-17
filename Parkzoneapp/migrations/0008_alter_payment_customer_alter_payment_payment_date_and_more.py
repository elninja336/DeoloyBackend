# Generated by Django 5.1.4 on 2025-01-19 09:39

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parkzoneapp', '0007_payment_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Parkzoneapp.customer'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
