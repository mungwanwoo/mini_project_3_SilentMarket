# Generated by Django 5.1.3 on 2024-11-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silentmarket', '0002_remove_address_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimg',
            name='url',
            field=models.URLField(max_length=1000),
        ),
    ]
