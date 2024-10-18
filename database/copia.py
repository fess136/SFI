import os
import datetime
import subprocess
import shutil
import zipfile


def get_base_dir():
    return os.getenv('BASE_DIR', os.path.dirname(os.path.abspath(__file__)))

def get_db_config():
    return {
        'name': os.getenv('DB_NAME', 'db'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', '123456'),
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('DB_PORT', '3306'),
    }

def check_mysql_installed():
    try:
        subprocess.run(['mysql', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("MySQL no está instalado o no está en el PATH del sistema.")
        return False

def hacer_copia():
    if not check_mysql_installed():
        return

    BASE_DIR = get_base_dir()
    print(f"BASE_DIR: {BASE_DIR}")

    dt = datetime.datetime.now()
    print(f"Fecha y hora actual: {dt}")

    nombre = f"Copia_de_seguridad_{dt.strftime('%d-%m-%Y__%H-%M-%S')}"
    print(f"Nombre de la copia de seguridad: {nombre}")

    temp_dir = os.path.join(BASE_DIR, "temp_backup")
    os.makedirs(temp_dir, exist_ok=True)
    print(f"Directorio temporal creado: {temp_dir}")

    db_config = get_db_config()
    backup_file = os.path.join(temp_dir, f"{nombre}.sql")

    dump_command = [
        'mysqldump',
        '-h', db_config['host'],
        '-P', db_config['port'],
        '-u', db_config['user'],
        f"--password={db_config['password']}",
        db_config['name']
    ]

    try:
        with open(backup_file, 'w', encoding='utf-8') as f:
            subprocess.run(dump_command, stdout=f, check=True)
        print(f"Base de datos exportada a: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error al exportar la base de datos: {e}")
        return

    # Corregir la ruta de la carpeta database
    database_dir = os.path.join(BASE_DIR, "database")
    os.makedirs(database_dir, exist_ok=True)

    try:
        archivo_zip_path = os.path.join(database_dir, nombre)
        archivo_zip = shutil.make_archive(archivo_zip_path, 'zip', temp_dir)
        print(f"Archivo zip creado: {archivo_zip}")
    except Exception as e:
        print(f"Error al crear el archivo zip: {e}")
        return

    try:
        shutil.rmtree(temp_dir)
        print(f"Directorio temporal eliminado: {temp_dir}")
    except Exception as e:
        print(f"Error al eliminar el directorio temporal: {e}")

    try:
        comienzo = [archivo for archivo in os.listdir(database_dir) if archivo.endswith(".zip")]
        print("Archivos de respaldo creados:", comienzo)
    except Exception as e:
        print(f"Error al listar los archivos de respaldo: {e}")

    print(f"Copia de seguridad creada en: {archivo_zip}")




def restaurar_copia_seleccionada(nombre_copia_seleccionada):
    if not check_mysql_installed():
        return

    BASE_DIR = get_base_dir()
    ruta_copia_seguridad = os.path.join(BASE_DIR, "database", nombre_copia_seleccionada)

    if not os.path.isfile(ruta_copia_seguridad):
        print(f"El archivo de copia de seguridad '{ruta_copia_seguridad}' no se encontró.")
        return

    temp_dir = os.path.join(BASE_DIR, "temp_restore")
    os.makedirs(temp_dir, exist_ok=True)

    try:
        with zipfile.ZipFile(ruta_copia_seguridad, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        sql_backup_path = next((os.path.join(temp_dir, file) for file in os.listdir(temp_dir) if file.endswith(".sql")), None)

        if sql_backup_path is None:
            print(f"El archivo SQL no se encontró en la copia de seguridad.")
            return

        db_config = get_db_config()

        restore_command = [
            'mysql',
            '-h', db_config['host'],
            '-P', db_config['port'],
            '-u', db_config['user'],
            f"--password={db_config['password']}",
            db_config['name']
        ]

        with open(sql_backup_path, 'r', encoding='utf-8') as f:
            try:
                subprocess.run(restore_command, stdin=f, check=True)
                print(f"La base de datos ha sido restaurada desde la copia de seguridad '{nombre_copia_seleccionada}'.")
            except subprocess.CalledProcessError as e:
                print(f"Error al restaurar la base de datos: {e}")

    except Exception as e:
        print(f"Error durante la restauración: {e}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"Directorio temporal eliminado: {temp_dir}")