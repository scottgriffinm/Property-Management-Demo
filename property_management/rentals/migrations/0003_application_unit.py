# Generated by Django 5.1.7 on 2025-04-01 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_tenant_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='unit',
            field=models.CharField(default='100', max_length=10),
        ),
    ]
