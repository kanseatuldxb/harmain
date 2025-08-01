# Generated by Django 5.2.4 on 2025-07-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartlift', '0006_liftflooreventlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='energymeterlog',
            name='e_scale',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='energymeterlog',
            name='escale_high',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energymeterlog',
            name='escale_low',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energymeterlog',
            name='kwh_high',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energymeterlog',
            name='kwh_low',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energymeterlog',
            name='kwh_raw',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='energymeterlog',
            name='kwh_value',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
