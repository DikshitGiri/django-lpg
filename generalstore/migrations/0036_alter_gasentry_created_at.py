# Generated by Django 4.0.1 on 2022-06-26 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalstore', '0035_alter_gasondemand_customer_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasentry',
            name='created_at',
            field=models.DateTimeField(default=datetime.timezone, null=True),
        ),
    ]
