# Generated by Django 5.1.3 on 2024-11-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculos',
            name='categoria',
            field=models.CharField(choices=[('1', 'Particular'), ('2', 'Transporte'), ('3', 'Carga')], default='particular', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='marca',
            field=models.CharField(choices=[('1', 'Ford'), ('2', 'Fiat'), ('3', 'Chevrolet'), ('4', 'Toyota')], default='ford', max_length=20),
        ),
    ]
