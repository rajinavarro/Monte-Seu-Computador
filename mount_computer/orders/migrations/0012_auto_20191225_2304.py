# Generated by Django 3.0.1 on 2019-12-26 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20191222_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cpu',
        ),
        migrations.AddField(
            model_name='order',
            name='cpu',
            field=models.CharField(default='Default', max_length=200),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='order',
            name='motherboard',
        ),
        migrations.AddField(
            model_name='order',
            name='motherboard',
            field=models.CharField(default='Default', max_length=200),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='order',
            name='rammemory',
        ),
        migrations.AddField(
            model_name='order',
            name='rammemory',
            field=models.CharField(default='Default', max_length=200),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='order',
            name='videocard',
        ),
        migrations.AddField(
            model_name='order',
            name='videocard',
            field=models.CharField(default='Default', max_length=200),
            preserve_default=False,
        ),
    ]
