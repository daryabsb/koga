# Generated by Django 3.1.6 on 2021-02-03 12:23

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('condition', models.CharField(choices=[('01', 'NEW'), ('02', 'USED'), ('03', 'REFURBISHED'), ('04', 'BROKEN')], default='01', max_length=2)),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.image_file_path)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.department')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.assettype')),
            ],
        ),
    ]
