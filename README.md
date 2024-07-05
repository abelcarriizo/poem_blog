# Poem Blog API

## Descripción

Este proyecto es una API para un blog de poemas, donde los usuarios pueden publicar poemas, comentar en los poemas de otros usuarios, seguir a otros usuarios y dar "me gusta" a los poemas.

## Requisitos

- Python 3.x
- pip
- virtualenv
- MariaDB

## Instalación

1. Clona el repositorio:

```sh
git clone https://github.com/tu_usuario/poem_blog.git
```

2. Ejecuta el script de instalación:

```sh
./install.sh
```

3. Crea la base de datos en MariaDB:

```sql
CREATE DATABASE poem_blog;
```

4. Si prefieres, puedes importar la base de datos usando el archivo SQL proporcionado en `src/database`:

```sh
mysql -u tu_usuario -p poem_blog < src/database/poem_blog.sql
```

## Configuración

El script `install.sh` creará automáticamente un archivo `.env` para configurar las variables de entorno necesarias. Durante la ejecución del script, se te pedirá que ingreses el puerto para la aplicación Flask, el nombre de usuario de la base de datos y la contraseña.

## Uso

1. Inicia la aplicación:

```sh
./boot.sh
```

## Endpoints

### Usuarios

- **GET /users**: Obtiene todos los usuarios.
- **GET /user/<id>**: Obtiene un usuario por ID.
- **POST /users**: Crea un nuevo usuario.
- **PUT /user/<id>**: Actualiza un usuario existente.
- **DELETE /user/<id>**: Elimina un usuario.

### Poemas

- **GET /poems**: Obtiene todos los poemas.
- **GET /poem/<id>**: Obtiene un poema por ID.
- **POST /poems**: Crea un nuevo poema.
- **PUT /poem/<id>**: Actualiza un poema existente.
- **DELETE /poem/<id>**: Elimina un poema.

### Comentarios

- **GET /comments/poem/<poem_id>**: Obtiene todos los comentarios de un poema.
- **POST /comments/poem/<poem_id>**: Crea un nuevo comentario en un poema.
- **DELETE /comments/<comment_id>**: Elimina un comentario.

### Seguidores

- **GET /followers/user/<user_id>**: Obtiene los seguidores de un usuario.
- **POST /follow/user/<user_id>/follower/<follower_id>**: Un usuario sigue a otro usuario.
- **DELETE /follow/user/<user_id>/follower/<follower_id>**: Un usuario deja de seguir a otro usuario.

### Likes

- **POST /like/poem/<poem_id>/user/<user_id>**: Un usuario da "me gusta" a un poema.
- **DELETE /like/poem/<poem_id>/user/<user_id>**: Un usuario quita "me gusta" a un poema.
- **GET /likes/poem/<poem_id>**: Obtiene todos los "me gusta" de un poema.

> **⚠️ Advertencia:**
> - **Base de Datos**: Asegúrate de utilizar MariaDB para evitar problemas de compatibilidad. La conexión puede no funcionar correctamente con MySQL.
> - **Creación de Base de Datos**: Debes crear la base de datos `poem_blog` manualmente o importar la base de datos desde el archivo `src/database/poem_blog.sql`.


