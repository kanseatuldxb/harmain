# Generated by Django 5.2.4 on 2025-07-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartlift', '0007_energymeterlog_e_scale_energymeterlog_escale_high_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energymeterlog',
            name='e_scale',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energymeterlog',
            name='kwh_raw',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energymeterlog',
            name='kwh_value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
