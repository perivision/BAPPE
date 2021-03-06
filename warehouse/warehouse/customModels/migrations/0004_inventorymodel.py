# Generated by Django 3.0.5 on 2020-04-16 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customModels', '0003_auto_20200416_0318'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryModel',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=128)),
                ('item_count', models.CharField(max_length=128)),
                ('item_location', models.CharField(max_length=128)),
                ('item_count_type', models.CharField(max_length=128)),
                ('action_date', models.DateField(verbose_name='Date')),
                ('action_type', models.CharField(max_length=128)),
                ('action_auther', models.CharField(max_length=128)),
                ('action_contact', models.CharField(max_length=128)),
                ('item_in_transit', models.BooleanField(default=False)),
            ],
        ),
    ]
