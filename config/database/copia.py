
import datetime
import os
import shutil
import zipfile
from django.conf import settings
import tempfile
import subprocess



def hacer_copia():
    # Definir BASE_DIR como la ruta del directorio del proyecto
    BASE_DIR = settings.BASE_DIR
    print(f"BASE_DIR: {BASE_DIR}")

    # Obtener la fecha y hora actual
    dt = datetime.datetime.now()
    print(f"Fecha y hora actual: {dt}")

    # Crear un nombre para la copia de seguridad basado en la fecha y hora actual
    nombre = "Copia_de_seguridad_{}-{}-{}__{}-{}-{}".format(
        dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second
    )
    print(f"Nombre de la copia de seguridad: {nombre}")

    # Crear un directorio temporal para la copia de la base de datos
    temp_dir = os.path.join(BASE_DIR, "temp_backup")
    os.makedirs(temp_dir, exist_ok=True)
    print(f"Directorio temporal creado: {temp_dir}")

    # Definir los parámetros de conexión a la base de datos MySQL
    db_name = 'db'  # Nombre de la base de datos
    db_user = 'root'  # Usuario de MySQL
    db_password = '123456'  # Contraseña de MySQL
    db_host = 'localhost'  # Host de MySQL
    db_port = '3306'  # Puerto de MySQL

    # Definir el archivo de respaldo
    backup_file = os.path.join(temp_dir, f"{nombre}.sql")

    # Comando para realizar el volcado de la base de datos
    dump_command = [
        'mysqldump',
        '-h', db_host,
        '-P', db_port,
        '-u', db_user,
        f'--password={db_password}',
        db_name
    ]

    # Ejecutar el comando de volcado de la base de datos
    try:
        with open(backup_file, 'w', encoding='utf-8') as f:
            subprocess.run(dump_command, stdout=f, check=True)
        print(f"Base de datos exportada a: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error al exportar la base de datos: {e}")
        return

    # Crear un archivo zip del directorio temporal
    try:
        archivo_zip_path = os.path.join(BASE_DIR, "database", nombre)
        archivo_zip = shutil.make_archive(archivo_zip_path, 'zip', temp_dir)
        print(f"Archivo zip creado: {archivo_zip}")
    except Exception as e:
        print(f"Error al crear el archivo zip: {e}")
        return

    # Eliminar el directorio temporal
    try:
        shutil.rmtree(temp_dir)
        print(f"Directorio temporal eliminado: {temp_dir}")
    except Exception as e:
        print(f"Error al eliminar el directorio temporal: {e}")
        return

    # Lista para almacenar los nombres de archivos zip
    comienzo = []

    # Listar todos los archivos en el directorio actual y agregar los archivos zip a la lista
    try:
        total = os.listdir(os.path.join(BASE_DIR, "database"))
        for archivo in total:
            if archivo.endswith(".zip"):
                comienzo.append(archivo)

        print("Archivos de respaldo creados:", comienzo)
    except Exception as e:
        print(f"Error al listar los archivos de respaldo: {e}")
        return

    print(f"Copia de seguridad creada en: {archivo_zip}")




def restaurar_copia_seleccionada(nombre_copia_seleccionada):
    # Definir BASE_DIR como la ruta del directorio del proyecto
    BASE_DIR = settings.BASE_DIR
    ruta_copia_seguridad = os.path.join(BASE_DIR, "database", nombre_copia_seleccionada)

    if not os.path.isfile(ruta_copia_seguridad):
        raise FileNotFoundError(f"El archivo de copia de seguridad '{ruta_copia_seguridad}' no se encontró.")

    temp_dir = os.path.join(BASE_DIR, "temp_restore")
    os.makedirs(temp_dir, exist_ok=True)

    try:
        # Descomprimir el archivo zip
        with zipfile.ZipFile(ruta_copia_seguridad, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Buscar el archivo SQL en la copia descomprimida
        sql_backup_path = None
        for file in os.listdir(temp_dir):
            if file.endswith(".sql"):
                sql_backup_path = os.path.join(temp_dir, file)
                break

        if sql_backup_path is None:
            raise FileNotFoundError(f"El archivo SQL no se encontró en la copia de seguridad.")

        # Definir parámetros de conexión a la base de datos MySQL
        db_name = 'db'  # Nombre de la base de datos
        db_user = 'root'  # Usuario de MySQL
        db_password = '123456'  # Contraseña de MySQL
        db_host = 'localhost'  # Host de MySQL
        db_port = '3306'  # Puerto de MySQL

        # Restaurar la base de datos desde el archivo SQL
        restore_command = [
            'mysql',
            '-h', db_host,
            '-P', db_port,
            '-u', db_user,
            f'--password={db_password}',
            db_name
        ]

        with open(sql_backup_path, 'r', encoding='utf-8') as f:
            try:
                subprocess.run(restore_command, stdin=f, check=True)
                print(f"La base de datos ha sido restaurada desde la copia de seguridad '{nombre_copia_seleccionada}'.")
            except subprocess.CalledProcessError as e:
                print(f"Error al restaurar la base de datos: {e}")
                raise

    finally:
        # Eliminar el directorio temporal
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"Directorio temporal eliminado: {temp_dir}")