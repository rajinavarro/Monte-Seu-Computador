# Generated by Django 3.0.1 on 2019-12-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191222_1409'),
        ('orders', '0008_auto_20191222_1409'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='default', max_length=120),
        ),
        migrations.AlterField(
            model_name='order',
            name='cpu',
            field=models.ManyToManyField(to='products.Cpu'),
        ),
    ]
