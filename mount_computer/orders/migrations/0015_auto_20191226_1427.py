# Generated by Django 3.0.1 on 2019-12-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20191226_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rammemory',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='videocard',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
