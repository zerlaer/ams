# Generated by Django 3.2.3 on 2021-05-19 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0002_auto_20210519_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sipphone',
            name='sip_manufacturer',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='制造商'),
        ),
    ]