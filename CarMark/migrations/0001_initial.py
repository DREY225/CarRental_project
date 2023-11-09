# Generated by Django 4.2.7 on 2023-11-02 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CarMark.carmark')),
            ],
        ),
    ]
