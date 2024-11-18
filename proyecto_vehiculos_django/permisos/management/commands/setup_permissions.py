from typing import Any
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Configuración de Usuarios'
    
    def handle(self, *args, **kwargs):
        # Creación del usuario Admin con permisos completos
        admin_user, created = User.objects.get_or_create(
            username = 'admin',
            defaults={'email': 'admin@admin.cl', 'is_staff': True, 'is_superuser':True}
        )
        if created:
            admin_user.set_password('admin')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Usuario creado con éxito.'))
        else:
            self.stdout.write(self.style.WARNING('Usuario ya existe.'))
            
        # Crear grupos de Usuarios y sus permisos por defecto
        grupo_permisos = {
            'Usuario_comun' : ['view_vehiculos'],
            'Editor'        : ['view_vehiculos', 'add_vehiculos']
        }
        
        for grupo_nombre, permisos in grupo_permisos.items():
            grupo, creado = Group.objects.get_or_create(name=grupo_nombre)
            
            for permisos_codename in permisos:
                permiso = Permission.objects.get(codename=permisos_codename)
                grupo.permissions.add(permiso)
            
        if creado:
            self.stdout.write(self.style.SUCCESS(f'Grupo {grupo_nombre} creados con éxito y permisos asignados.'))
        else:
            self.stdout.write(self.style.WARNING(f'Grupo {grupo_nombre} ya esta registrado.'))
        
        admin_user.groups.add(Group.objects.get(name='Editor'))
        admin_user.is_staff = True
        admin_user.is_active = True
        admin_user.save()
        self.stdout.write(self.style.SUCCESS('Configuración inicial completada con éxito'))
        