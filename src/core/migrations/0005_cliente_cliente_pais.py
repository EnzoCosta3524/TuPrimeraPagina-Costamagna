# Generated by Django 5.1.7 on 2025-03-17 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cliente_pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.pais'),
        ),
    ]
