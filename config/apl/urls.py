from django.urls import path
from apl.views import *
from apl.vista.tipo.views import listar_tipo

app_name = 'apl'
urlpatterns = [
    # path("uno/",vista1, name='vista1'),
    # path("dos/",vista2, name='vista2'),
    # path("tres/",vista3, name='vista3'),
    path("tipo/listar", listar_tipo, name = "listar_tipo")

]
