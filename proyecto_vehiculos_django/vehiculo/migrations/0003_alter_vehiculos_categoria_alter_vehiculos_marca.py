# Generated by Django 5.1.3 on 2024-11-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_alter_vehiculos_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculos',
            name='categoria',
            field=models.CharField(choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], default='particular', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='marca',
            field=models.CharField(choices=[('Ford', 'Ford'), ('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Toyota', 'Toyota')], default='ford', max_length=20),
        ),
    ]
