# Generated by Django 5.1.4 on 2025-01-16 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parkzoneapp', '0005_alter_customer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkinglot',
            name='slotNumber',
            field=models.CharField(max_length=50),
        ),
    ]
