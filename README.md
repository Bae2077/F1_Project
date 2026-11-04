# 🏎️ F1 Hub

Aplicación web desarrollada con **Django** que permite consultar y administrar información relacionada con la Fórmula 1, incluyendo pilotos, escuderías y temporadas.

El proyecto corresponde a la evolución de una aplicación desarrollada inicialmente para la Evaluación Sumativa N.º 2 de Programación Back End, incorporando nuevas funcionalidades de autenticación, gestión de usuarios, permisos y administración personalizada de datos para la Evaluación Sumativa N.º 3.

## Funcionalidades

- Visualización de pilotos y escuderías mediante tarjetas Bootstrap.
- Búsqueda de pilotos y escuderías.
- Selección y consulta de temporadas.
- Mantenedores personalizados para pilotos y escuderías.
- Operaciones CRUD: crear, consultar, modificar y eliminar registros.
- Gestión de relaciones entre pilotos, escuderías y temporadas.
- Registro de participaciones de pilotos en distintas temporadas.
- Inicio y cierre de sesión.
- Creación y gestión de usuarios.
- Recuperación de contraseñas mediante enlaces seguros.
- Acceso diferenciado según el perfil del usuario.
- Protección de vistas mediante permisos y autenticación.

## Perfiles de usuario

El sistema contempla tres perfiles con distintos niveles de acceso:

| Perfil | Permisos principales |
|---|---|
| Administrador | Gestión de usuarios, pilotos y escuderías. |
| Supervisor | Administración de pilotos y escuderías. |
| Administrativo | Consulta de información sin permisos de modificación. |

Cada perfil cuenta con un panel de usuario que presenta las opciones disponibles según sus permisos.

## Tecnologías utilizadas

| Tecnología | Función |
|---|---|
| Python | Lenguaje de programación |
| Django | Framework web, autenticación y ORM |
| HTML, CSS y Bootstrap | Interfaz de usuario |
| SQLite | Base de datos para desarrollo local |
| MariaDB | Base de datos relacional en AWS |
| phpMyAdmin | Verificación de tablas y registros |
| Git y GitHub | Control de versiones |
| AWS EC2 | Infraestructura cloud |
| Ubuntu | Sistema operativo del servidor |
| Gunicorn | Servidor de aplicaciones |
| Nginx | Servidor web y proxy inverso |

## Estructura del proyecto

```text
F1_Project/
├── escuderias/
├── f1_hub/
├── old_data/
├── pilotos/
├── usuarios/
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

Las aplicaciones principales son:

- **pilotos:** administra la información de pilotos, temporadas y participaciones.
- **escuderias:** administra los equipos de Fórmula 1 y sus datos.
- **usuarios:** gestiona la autenticación, los perfiles, la creación de usuarios y la recuperación de contraseñas.

## Modelos de datos

El proyecto utiliza cuatro entidades principales:

- **Piloto:** nombre, nacionalidad, fotografía e información.
- **Escuderia:** nombre, país, logotipo e información.
- **Temporada:** año y descripción.
- **ParticipacionPiloto:** relaciona un piloto con una escudería durante una temporada e incluye su número de competición.

Las relaciones se implementan mediante claves foráneas de Django ORM, permitiendo mantener la integridad de los datos y gestionar las participaciones entre entidades relacionadas.

## Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/shinyx17/F1_Project.git
cd F1_Project
```

### 2. Crear y activar un entorno virtual

En Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

En Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DJANGO_SECRET_KEY=tu_clave_secreta
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Por defecto, el proyecto utiliza SQLite si no se definen las variables de conexión a MariaDB.

Para utilizar MariaDB, configurar también:

```env
DB_NAME=nombre_base_datos
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=3306
```

**Importante:** nunca subir el archivo `.env` ni las contraseñas al repositorio.

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

### 6. Importar datos iniciales

Si se dispone del conjunto de datos iniciales del proyecto:

```bash
python manage.py importar_datos
```

### 7. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` en el navegador.

Para crear un usuario administrador inicial:

```bash
python manage.py createsuperuser
```

## Recuperación de contraseñas

El sistema incorpora el mecanismo de recuperación de contraseñas de Django, que permite:

1. Solicitar la recuperación desde el inicio de sesión.
2. Generar un enlace con un token de seguridad.
3. Validar el enlace antes de permitir el cambio.
4. Registrar una nueva contraseña.
5. Confirmar que la contraseña fue actualizada correctamente.

Durante las pruebas locales se utiliza el backend de correo por consola de Django, que permite visualizar los mensajes y enlaces generados directamente en la terminal. Para el envío real de correos se requiere configurar un servicio SMTP.

## Despliegue en AWS

La aplicación fue desplegada en una instancia **Amazon EC2 con Ubuntu 24.04 LTS**.

Su arquitectura utiliza:

1. **Nginx:** recibe las solicitudes HTTP.
2. **Gunicorn:** ejecuta la aplicación Django.
3. **Django ORM:** gestiona las consultas y operaciones sobre los modelos.
4. **MariaDB:** almacena la información de manera persistente.
5. **phpMyAdmin:** permite verificar la estructura y los registros de la base de datos.

Gunicorn está configurado como servicio de `systemd` para iniciarse automáticamente con la instancia.

El acceso administrativo a phpMyAdmin se realiza mediante un túnel SSH.

La dirección IP pública de EC2 puede cambiar cuando la instancia se detiene y vuelve a iniciarse.

## Control de versiones

El código fuente se administra mediante Git y GitHub, utilizando commits para registrar los avances y cambios del proyecto.

**Repositorio:** https://github.com/shinyx17/F1_Project

## Uso de inteligencia artificial

Durante el desarrollo se utilizó ChatGPT como herramienta de apoyo para:

- Orientar la implementación de modelos y relaciones.
- Revisar configuraciones de Django.
- Resolver errores de desarrollo y despliegue.
- Apoyar la configuración de AWS, Gunicorn, Nginx y MariaDB.
- Elaborar documentación técnica.

Las soluciones propuestas fueron aplicadas y comprobadas mediante pruebas del proyecto.

## Estado del proyecto

F1 Hub cuenta con visualización pública de información, mantenedores personalizados, gestión de usuarios, autenticación, permisos diferenciados, recuperación de contraseñas y una transacción entre entidades relacionadas.

El proyecto utiliza persistencia mediante una base de datos relacional y contempla su despliegue en infraestructura AWS EC2.

Proyecto desarrollado con fines académicos para la asignatura **Programación Back End**.