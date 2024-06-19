# Proyecto API REST con Flask, SQLAlchemy y JWT

<div align="center">
<a href="https://www.python.org/" target="_blank">
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="django" alt="django" width="40" height="40"/>
</a>
<a href="https://flask.palletsprojects.com/en/2.1.x/" target="_blank">
<img src="https://github.com/devicons/devicon/blob/master/icons/flask/flask-original.svg" title="flask" alt="flask" width="40" height="40"/>
</a>
<a href="https://www.microsoft.com/en-us/sql-server" target="_blank">
<img src="https://github.com/devicons/devicon/blob/master/icons/microsoftsqlserver/microsoftsqlserver-plain-wordmark.svg" title="microsoftsqlserver" alt="microsoftsqlserver" width="40" height="40"/>
</a>
</div>


Este proyecto implementa una API REST en Python utilizando Flask, SQLAlchemy para la gestión de la base de datos SQL Server, y JWT para la autenticación de usuarios. La API permite registrar usuarios, iniciar sesión, crear tareas y listar tareas asociadas a cada usuario.

## Requisitos del Proyecto

1. **Registro de Usuario (register)**:
   - Endpoint `/register` para registrar nuevos usuarios en la base de datos.
   - Campos requeridos: `usuario` y `contraseña`.
   - Validación de usuario único antes de registrar.

2. **Inicio de Sesión (login)**:
   - Endpoint `/login` para autenticar usuarios y generar un token JWT.
   - Campos requeridos: `usuario` y `contraseña`.
   - Verificación de credenciales de usuario.

3. **Creación de Tareas (tasks)**:
   - Endpoint `/tasks` para crear nuevas tareas asociadas al usuario autenticado.
   - Campos requeridos: `titulo` de la tarea.
   - Registro de `descripcion`, `fecha_creacion` automáticamente.

4. **Listado de Tareas (tasks)**:
   - Endpoint `/tasks` para obtener todas las tareas del usuario autenticado.
   - Devolución de lista de tareas con campos: `id_tarea`, `titulo`, `descripcion`, `fecha_creacion`.

5. **Base de Datos**:
   - Utilización de SQL Server con las tablas en esquemas `usuario` y `tareas`.
   - Conexión configurada en `config.py` utilizando SQLAlchemy.

6. **Seguridad**:
   - Uso de JWT para autenticación y autorización de usuarios.
   - Generación de tokens JWT al autenticar usuarios en `/login`.
   - Protección de endpoints utilizando `jwt_required()`.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
project/
│
├── app.py
├── config.py
├── models.py
├── services.py
├── requirements.txt
├── .env
└── routes/
├── init.py
├── auth.py
└── tasks.py
```


- **`app.py`**: Archivo principal de la aplicación que configura y ejecuta la aplicación Flask.
- **`config.py`**: Configuración de la base de datos y variables de la aplicación.
- **`models.py`**: Definición de los modelos de SQLAlchemy para las tablas `Usuario` y `Tarea`.
- **`services.py`**: Lógica de negocio y servicios para manejar operaciones como registro de usuarios, autenticación, creación y obtención de tareas.
- **`routes/`**: Carpeta que contiene los blueprints de los endpoints de la API.
  - **`auth.py`**: Blueprint para las rutas relacionadas con la autenticación (`/register`, `/login`).
  - **`tasks.py`**: Blueprint para las rutas relacionadas con las tareas (`/tasks`).


## Replica la base de datos 
Para replicar la base de datos ejeuta [este script](/database.sql)
 en el managment de SQL Server


## Configuración del Entorno

1. Clona el repositorio desde GitHub:

   ```bash
   https://github.com/MrDavidAlv/API-REST-PYTHON-FLASK.git

2. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt

3. Configura las variables de entorno en el archivo .env:

   ```bash
    DATABASE_URI="string de conexión a SQL Server"
    SECRET_KEY=your_secret_key
    JWT_SECRET_KEY=your_jwt_secret_key

4. Ejecuta la aplicación:

    ```bash
    python app.py


## API

1. Registro de Usuario:
```
POST /register
Content-Type: application/json

{
    "usuario": "ejemplo_usuario",
    "contraseña": "password123"
}
```

2. Inicio de Sesión:
```
POST /login
Content-Type: application/json

{
    "usuario": "ejemplo_usuario",
    "contraseña": "password123"
}
```

3. Creación de Tarea:
```
POST /tasks
Content-Type: application/json
Authorization: Bearer <tu_token_jwt>

{
    "titulo": "Nueva tarea",
    "descripcion": "Descripción de la tarea"
}
```

4. Listado de Tareas:
```
GET /tasks
Authorization: Bearer <tu_token_jwt>
```
