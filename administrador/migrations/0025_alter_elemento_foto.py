# Generated by Django 4.0.3 on 2022-05-23 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0024_alter_elemento_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='foto',
            field=models.ImageField(blank=True, upload_to='elemento'),
        ),
    ]