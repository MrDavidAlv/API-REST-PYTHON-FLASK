from models import db, Usuario, Tarea
from datetime import datetime

def register_user(data):
    if not data or not data.get('usuario') or not data.get('contraseña'):
        return {"msg": "Usuario y contraseña son requeridos"}, 400

    if Usuario.query.filter_by(usuario=data['usuario']).first():
        return {"msg": "Usuario ya existe"}, 400

    new_user = Usuario(usuario=data['usuario'])
    new_user.set_password(data['contraseña'])
    db.session.add(new_user)
    db.session.commit()

    return {"msg": "Usuario registrado exitosamente"}, 201

def authenticate_user(data):
    if not data or not data.get('usuario') or not data.get('contraseña'):
        return {"msg": "Usuario y contraseña son requeridos"}, 400

    user = Usuario.query.filter_by(usuario=data['usuario']).first()
    if not user or not user.check_password(data['contraseña']):
        return {"msg": "Credenciales inválidas"}, 401

    return user

def create_task(data, user_id):
    new_task = Tarea(
        titulo=data['titulo'],
        descripcion=data.get('descripcion'),
        fecha_creacion=datetime.utcnow(),
        id_usuario=user_id
    )
    db.session.add(new_task)
    db.session.commit()

    return {"msg": "Tarea creada exitosamente"}, 201

def get_user_tasks(user_id):
    tasks = Tarea.query.filter_by(id_usuario=user_id).all()
    tasks_list = [
        {"id_tarea": task.id_tarea, "titulo": task.titulo, "descripcion": task.descripcion, "fecha_creacion": task.fecha_creacion}
        for task in tasks
    ]
    return tasks_list
