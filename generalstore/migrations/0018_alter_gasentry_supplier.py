# Generated by Django 4.0.1 on 2022-06-01 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generalstore', '0017_alter_gasentry_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasentry',
            name='supplier',
            field=models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
