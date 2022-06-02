# Generated by Django 4.0.3 on 2022-05-11 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Electrodomesticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('referencia', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.CharField(max_length=50)),
                ('porcentaje_ganancia', models.CharField(max_length=6)),
                ('foto', models.CharField(max_length=6, unique=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=20, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=20, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='TipoElemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=10, unique=True)),
                ('tipodoc', models.CharField(choices=[('C.C.', 'Cedula'), ('T.I.', 'Tarjeta'), ('R.C.', 'Registro Civil'), ('C.E.', 'Cedula Extranjeria')], max_length=20, verbose_name='Tipo de documento')),
                ('rol', models.CharField(choices=[('Administrador', 'Administrador'), ('Trabajador', 'Trabajador'), ('Proveedor', 'Proveedor'), ('Cliente', 'Cliente')], max_length=20, verbose_name='Rol')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('especializacion', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=20, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.CharField(max_length=500, verbose_name='Diagnostico')),
                ('tiposervicio', models.CharField(choices=[('Reparación', 'Reparación'), ('Mantenimiento', 'Mantenimiento')], max_length=20, verbose_name='Tipo de Servicio')),
                ('cantidad', models.CharField(max_length=10, verbose_name='Cantidad')),
                ('fallas_basicas', models.CharField(max_length=255, verbose_name='Falla Basica')),
                ('fecha_entrega', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha de Entrega')),
                ('electrodomesticos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.electrodomesticos', verbose_name='Electrodomesticos')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=15)),
                ('compraoventa', models.CharField(choices=[('Compra', 'Compra'), ('Venta', 'Venta')], max_length=6, verbose_name='CompraoVenta')),
                ('monto', models.CharField(max_length=15)),
                ('fecha', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha de Registro')),
                ('elemento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.elemento', verbose_name='Elemento')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.usuario', verbose_name='Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='elemento',
            name='tipo_elemento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.tipoelemento', verbose_name='Tipo Producto'),
        ),
        migrations.AddField(
            model_name='electrodomesticos',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.marca', verbose_name='Marca'),
        ),
    ]