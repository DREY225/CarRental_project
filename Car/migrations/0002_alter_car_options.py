# Generated by Django 4.2.7 on 2023-11-02 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Voiture', 'verbose_name_plural': 'Voitures'},
        ),
    ]
