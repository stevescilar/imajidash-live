# Generated by Django 4.0.3 on 2022-06-15 08:35

import dashboard.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DispatchCargoChina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('receipt_no', models.CharField(blank=True, default=dashboard.utils.receipt_no, editable=False, max_length=6, null=True, unique=True)),
                ('cbm', models.CharField(max_length=200, null=True)),
                ('ctns', models.CharField(max_length=200, null=True)),
                ('weight', models.CharField(max_length=200, null=True)),
                ('shipping_mark', models.CharField(blank=True, default=dashboard.utils.shipping_mark, editable=False, max_length=6, null=True, unique=True)),
                ('container_number', models.CharField(max_length=50, verbose_name='Cont-N0:')),
                ('remark', models.TextField(null=True, verbose_name='Remarks')),
                ('client_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispatchchina_name', to='dashboard.client')),
            ],
        ),
        migrations.CreateModel(
            name='SalesAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.client')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('participant', models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReceivedCargoKenya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cbm', models.CharField(max_length=200, null=True)),
                ('ctns', models.CharField(max_length=200, null=True)),
                ('weight', models.CharField(max_length=200)),
                ('remark', models.TextField(null=True)),
                ('client_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.client')),
                ('goods', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.dispatchcargochina')),
            ],
        ),
        migrations.CreateModel(
            name='ReceivedCargoChina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('goods', models.CharField(max_length=200, null=True)),
                ('cbm', models.IntegerField(max_length=200, null=True)),
                ('ctns', models.IntegerField(max_length=200, null=True)),
                ('weight', models.IntegerField(max_length=200, null=True)),
                ('remark', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('client_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.client')),
                ('sales_agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.salesagent')),
            ],
        ),
        migrations.CreateModel(
            name='MsgFromChina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send', models.BooleanField(default=False)),
                ('client_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_rchina', to='dashboard.receivedcargochina')),
                ('goods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.receivedcargochina')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cargo_is_active', to='dashboard.receivedcargochina')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('remark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.remark')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImajiAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DispatchCargoKenya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('delivery_number', models.CharField(max_length=50)),
                ('cbm', models.CharField(max_length=200, null=True)),
                ('ctns', models.CharField(max_length=200, null=True)),
                ('weight', models.CharField(max_length=200, null=True)),
                ('received_by', models.CharField(max_length=50, null=True)),
                ('Receiver_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('remark', models.TextField(null=True, verbose_name='Remarks')),
                ('client_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispatch_name', to='dashboard.client')),
                ('goods', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.receivedcargokenya')),
            ],
        ),
        migrations.AddField(
            model_name='dispatchcargochina',
            name='goods',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.receivedcargochina'),
        ),
        migrations.AddField(
            model_name='client',
            name='sales_agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.salesagent'),
        ),
    ]