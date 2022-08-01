# Generated by Django 4.0.3 on 2022-05-23 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='carrito')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descuento', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=64)),
            ],
        ),
    ]
