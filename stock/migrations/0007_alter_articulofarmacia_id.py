# Generated by Django 3.2.9 on 2022-01-03 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_alter_articulofarmacia_fecharda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulofarmacia',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]