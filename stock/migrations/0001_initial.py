# Generated by Django 3.2.9 on 2022-01-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaFarmacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categoriaFarma',
                'verbose_name_plural': 'categoriasFarma',
            },
        ),
        migrations.CreateModel(
            name='ArticuloFarmacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArticulo', models.CharField(max_length=75)),
                ('cantidad', models.IntegerField()),
                ('agnoCaducidad', models.IntegerField()),
                ('mesCaducidad', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('categorias', models.ManyToManyField(to='stock.CategoriaFarmacia')),
            ],
            options={
                'verbose_name': 'ArticuloFarmacia',
                'verbose_name_plural': 'ArticulosFarmacia',
            },
        ),
    ]
