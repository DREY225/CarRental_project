# Generated by Django 4.2.7 on 2023-11-02 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarMark', '0002_alter_carmark_options_remove_carmark_model'),
        ('CarModel', '0002_alter_carmodel_options_remove_carmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarMark.carmark'),
        ),
    ]
