import datetime
import os
import shutil

# Obtener la fecha y hora actual
dt = datetime.datetime.now()

# Crear un nombre para la copia de seguridad basado en la fecha y hora actual
nombre = "Copia_de_seguridad_creada_el_dia_{}_del_año_{}_y_la_hora_{}".format(dt.day, dt.year, dt.hour)

# Crear un archivo zip de la carpeta 'database'
shutil.make_archive(nombre, "zip", "database")

# Lista para almacenar los nombres de archivos zip
comienzo = []

# Listar todos los archivos en el directorio actual
total = os.listdir()

# # Buscar archivos que terminan en .zip
# for i in total:
#     if i.endswith(".zip"):
#         comienzo.append(i)

