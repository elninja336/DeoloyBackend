# Generated by Django 5.1.4 on 2025-01-16 04:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parkzoneapp', '0006_alter_parkinglot_slotnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Parkzoneapp.customer'),
        ),
    ]
