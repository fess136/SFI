from django.urls import path
from apl.views import*

urlpatterns = [
    path("uno/",vista1, name='vista1'),
    path("dos/",vista2, name='vista2')
]
