# Generated by Django 4.1 on 2022-08-20 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_receiver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(max_length=1024, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='measureunit',
            name='id',
            field=models.CharField(max_length=1024, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(max_length=1024, primary_key=True, serialize=False, unique=True),
        ),
    ]
