def editor_group_processor(request):
    # Si el usuario no está autenticado, devolvemos False
    if not request.user.is_authenticated:
        return {'user_is_editor': False, 'user_is_authenticated': False}
    
    # Comprobamos si el usuario pertenece al grupo 'Editor'
    is_editor = request.user.groups.filter(name='Editor').exists()
    return {'user_is_editor': is_editor, 'user_is_authenticated': True}