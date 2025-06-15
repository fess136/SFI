FROM python:3.12.3

# Crear el directorio
RUN mkdir -p /home/app

# Establecer la ruta del proyecto
WORKDIR /home/app

# Puerto expuesto según la configuración del puerto del proyecto
EXPOSE 8000

# Instala librerías necesarias
COPY requirements.txt /home/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/app

# Crear directorio para archivos estáticos
RUN mkdir -p /home/app/staticfiles

RUN echo '#!/bin/bash\n\
# Recolecta archivos estáticos\n\
python manage.py collectstatic --noinput\n\
# Crea tablas\n\
python manage.py migrate\n\
# Crea superusuario\n\
python manage.py createsuperuser --noinput\n\
# Levanta el proyecto\n\
python manage.py runserver 0.0.0.0:8000' > start.sh

# Crea permisos para la ejecución del archivo
RUN chmod +x start.sh

CMD ["./start.sh"]