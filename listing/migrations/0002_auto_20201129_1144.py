# Generated by Django 3.1.3 on 2020-11-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='zip_code',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
