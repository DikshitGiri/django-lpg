# Generated by Django 4.0.1 on 2022-06-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalstore', '0039_alter_gasondemand_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasondemand',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
