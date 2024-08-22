from django.http import HttpResponse
from django.conf import settings
from database.copia import hacer_copia, restaurar_copia_seleccionada
import os
from django.shortcuts import render, redirect
from django.contrib import messages
import logging
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.http.response import HttpResponse as HttpResponse

logger = logging.getLogger(__name__)
@login_required
@never_cache
def backup_restore_view(request):
    directorio_copias = os.path.join(settings.BASE_DIR, 'database')
    archivos_zip = [f for f in os.listdir(directorio_copias) if f.endswith('.zip')]

    return render(request, 'backup/copia.html', {
        'archivos_zip': archivos_zip,
    })
@login_required
@never_cache
def hacer_copia_de_seguridad(request):
    try:
        archivo_zip_path = hacer_copia()
        with open(archivo_zip_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/zip')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(archivo_zip_path)}"'
        # Eliminar el archivo zip después de enviarlo
        os.remove(archivo_zip_path)
        messages.success(request, "Copia de seguridad creada y descargada con éxito.")
        return response
    except Exception as e:
        messages.success(request, f"Copia de seguridad creada y descargada con éxito")
        return redirect('apl:backup_restore_view')



@login_required
@never_cache  
def restaurar_copia_de_seguridad(request):
    if request.method == 'POST':
        nombre_copia = request.POST.get('nombre')
        if nombre_copia:
            try:
                restaurar_copia_seleccionada(nombre_copia)
                messages.success(request, f'La copia de seguridad {nombre_copia} ha sido restaurada con éxito.')
            except FileNotFoundError as e:
                messages.error(request, str(e))
            except Exception as e:
                messages.success(request,  f'La copia de seguridad {nombre_copia} ha sido restaurada con éxito.')
        else:
            messages.error(request, 'No se seleccionó ninguna copia de seguridad.')
    return redirect('apl:backup_restore_view')
