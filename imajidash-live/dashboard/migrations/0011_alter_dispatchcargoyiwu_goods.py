# Generated by Django 4.0.3 on 2022-07-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_dispatchcargoyiwu_shipping_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatchcargoyiwu',
            name='goods',
            field=models.TextField(blank=True, null=True),
        ),
    ]