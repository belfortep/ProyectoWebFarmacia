# Generated by Django 3.2.9 on 2022-01-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20220103_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulofarmacia',
            name='fecharda',
            field=models.DateField(blank=True, null=True),
        ),
    ]