# Generated by Django 4.0.1 on 2022-06-01 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generalstore', '0007_alter_gasentry_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='category',
        ),
    ]
