# Generated by Django 2.1.2 on 2019-02-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]