from django.urls import path

from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

#enlazar urls del proyecto al de la aplicacion

urlpatterns = [
    
    


]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)      #añadiendo las imagenes que creo.