# Generated by Django 3.0.1 on 2019-12-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20191225_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='rammemory2',
            field=models.CharField(default='Default', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='cpu',
            field=models.CharField(max_length=200, verbose_name='cpu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='motherboard',
            field=models.CharField(max_length=200, verbose_name='motherboard'),
        ),
    ]
