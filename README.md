# SFI
#Gestor de inventario y facturacion local

# Tecnologias usados
- python (framework django)
- Html
- Javascript
- Css
- Docker
- Git
- Github

# Ejecucion

Para ejecutar ese proyecto se puede ejecutar de dos maneras; con docker o de forma local

# Ejecucion con Docker (recomendado):

- Antes de levantar el docker se debe un archivo .env con variables de entonrno necesarios para el levantamiento del proyecto
  esta es una plantilla de las variables

    # Variables para conectar la base de datos
    MYSQL_ROOT_PASSWORD=123456
    MYSQL_DATABASE=Prueba_SFI_db
    MYSQL_USER=usuario
    MYSQL_PASSWORD=123456
    MYSQL_PORT=3306 # No cambiar
    MYSQL_HOST=sfi-db # No cambiar

    # Estas credenciales son para poder iniciar sesion con el super usuario
    SUPERUSER_USERNAME=usuario
    SUPERUSER_EMAIL=ejemplo@gmail.com
    SUPERUSER_PASSWORD=123456

- la ubicacion del archivo debe estar en la raiz del proyecto, es decir, de la siguiente manera
    SFI/
    ├── apl/
    ├── config/
    ├── dashboard/
    ├── database/
    ├── inicio/
    ├── login/
    ├── static/
    ├── staticfiles/
    ├── temp_backup/
    ├── templates/
    ├── .env  <------------ Ubicacion
    ├── manage.py
    ├── requirements.txt
    ├── Dockerfile
    ├── docker-compose.yml
    └── README.md
- Despues de crear el archivo .env ejecutar el comando "docker compose up" y despues de que se levante el docker
  ingresar a este link http://localhost:8000/
# Ejecucion Local:

- En caso de necesitar ejecutarlo de forma local se debe tener de igual forma el archivo .env con las siguientes variables
  para la conexión a la base de datos:

    MYSQL_DATABASE=Prueba_SFI_db
    MYSQL_USER=usuario
    MYSQL_PASSWORD=123456
    MYSQL_PORT=3306 
    MYSQL_HOST=localhost

- Una vez hecho esto se debe ejecutar los siguientes comandos:

- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

- Despues de crear el archivo .env y ejecutar los comandos ingresar a este link http://localhost:8000/