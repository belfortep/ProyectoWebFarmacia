# Generated by Django 3.2.9 on 2022-01-03 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_alter_articulofarmacia_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulofarmacia',
            name='id',
            field=models.FloatField(primary_key=True, serialize=False),
        ),
    ]