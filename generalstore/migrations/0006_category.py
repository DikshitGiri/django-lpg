# Generated by Django 4.0.1 on 2022-05-29 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalstore', '0005_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
    ]
