# Generated by Django 2.1.4 on 2019-02-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20190202_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]