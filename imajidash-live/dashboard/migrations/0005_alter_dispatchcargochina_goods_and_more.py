# Generated by Django 4.0.3 on 2022-07-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_salesagent_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatchcargochina',
            name='goods',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='dispatchcargochina',
            name='receipt_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='dispatchcargochina',
            name='shipping_mark',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
