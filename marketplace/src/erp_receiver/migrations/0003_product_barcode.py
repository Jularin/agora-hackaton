# Generated by Django 4.1 on 2022-08-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_receiver', '0002_alter_category_id_alter_measureunit_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.IntegerField(blank=True, null=True, verbose_name='Штрихкод'),
        ),
    ]
