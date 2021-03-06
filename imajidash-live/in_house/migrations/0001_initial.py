# Generated by Django 4.0.3 on 2022-07-04 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0003_receivedcargoyiwu_dispatchcargoyiwu'),
    ]

    operations = [
        migrations.CreateModel(
            name='offloadedCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_origin', models.CharField(choices=[('Yiwu', 'Yiwu'), ('Quanzhou', 'Quanzhou')], default='Quanzhou', max_length=10)),
                ('container_number', models.CharField(max_length=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('goods', models.CharField(max_length=200, null=True)),
                ('cbm', models.IntegerField(null=True)),
                ('ctns', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('amount', models.FloatField(default=False)),
                ('remark', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('client_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.client')),
                ('sales_agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.salesagent')),
            ],
        ),
    ]
