# Generated by Django 4.1 on 2022-08-21 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='marketplace_id',
            new_name='queue_name',
        ),
    ]
