
import datetime
import os
import shutil
import zipfile
from django.conf import settings
import tempfile


def hacer_copia():
    # Definir BASE_DIR como la ruta del directorio del proyecto
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(f"BASE_DIR: {BASE_DIR}")

    # Ruta al archivo de base de datos
    db_path = os.path.join(BASE_DIR, 'db.sqlite3')
    print(f"db_path: {db_path}")

    # Verificar si el archivo de base de datos existe
    if not os.path.isfile(db_path):
        print(f"Error: El archivo de base de datos '{db_path}' no se encontró.")
        return

    # Obtener la fecha y hora actual
    dt = datetime.datetime.now()
    print(f"Fecha y hora actual: {dt}")

    # Crear un nombre para la copia de seguridad basado en la fecha y hora actual
    nombre = "Copia de seguridad {}-{}-{}  {}{}".format(dt.day,dt.month, dt.year, dt.hour,dt.minute)
    print(f"Nombre de la copia de seguridad: {nombre}")

    # Crear un directorio temporal para la copia de la base de datos
    temp_dir = os.path.join(BASE_DIR, "temp_backup")
    os.makedirs(temp_dir, exist_ok=True)
    print(f"Directorio temporal creado: {temp_dir}")

    # Copiar la base de datos al directorio temporal
    try:
        shutil.copy2(db_path, temp_dir)
        print("Base de datos copiada al directorio temporal.")
    except Exception as e:
        print(f"Error al copiar la base de datos: {e}")
        return

    # Crear un archivo zip del directorio temporal
    try:
        archivo_zip_path = os.path.join(BASE_DIR, nombre)
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
        total = os.listdir(BASE_DIR)
        for archivo in total:
            if archivo.endswith(".zip"):
                comienzo.append(archivo)

        print("Archivos de respaldo creados:", comienzo)
    except Exception as e:
        print(f"Error al listar los archivos de respaldo: {e}")
        return

    print(f"Copia de seguridad creada en: {archivo_zip}")




def restaurar_copia_seleccionada(nombre_copia_seleccionada):
    
    BASE_DIR = settings.BASE_DIR
    ruta_copia_seguridad = os.path.join( BASE_DIR,"database", nombre_copia_seleccionada)

    if not os.path.isfile(ruta_copia_seguridad):
        raise FileNotFoundError(f"El archivo de copia de seguridad '{ruta_copia_seguridad}' no se encontró.")

    temp_dir = os.path.join(BASE_DIR, "temp_restore")
    os.makedirs(temp_dir, exist_ok=True)
    try:
        with zipfile.ZipFile(ruta_copia_seguridad, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        db_backup_path = os.path.join(temp_dir, 'db.sqlite3')
        if not os.path.isfile(db_backup_path):
            raise FileNotFoundError(f"El archivo de base de datos descomprimido 'db.sqlite3' no se encontró en la copia de seguridad.")

        db_path = os.path.join(BASE_DIR,"database", 'db.sqlite3')
        
        print (db_backup_path)
        db_backup_current = os.path.join(BASE_DIR,"database", 'db_backup_current.sqlite3')
        print (db_backup_current)
        shutil.copy2(db_path, db_backup_current)
        print ('asdfgh')

        # Usar un archivo temporal
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copy2(db_backup_path, tmp_file.name)
            shutil.move(tmp_file.name, db_path)
        raise Exception(f"Error inesperado al restaurar la copia de seguridad: {str(e)}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
    
        print(f"La base de datos ha sido restaurada desde la copia de seguridad '{nombre_copia_seleccionada}'.")
        print(f"Se ha creado una copia de seguridad del archivo actual en '{db_backup_current}'.")




