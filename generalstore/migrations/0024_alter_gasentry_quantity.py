# Generated by Django 4.0.1 on 2022-06-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalstore', '0023_gasentry_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasentry',
            name='quantity',
            field=models.IntegerField(blank=True, null=b'I01\n'),
        ),
    ]
