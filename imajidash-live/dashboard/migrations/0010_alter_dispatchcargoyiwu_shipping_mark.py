# Generated by Django 4.0.3 on 2022-07-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_dispatchcargoyiwu_cbm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatchcargoyiwu',
            name='shipping_mark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]