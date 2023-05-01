from django.urls import path,include
from .views import *
from .form import ClientForm
from django.conf import settings
from django.conf.urls.static import static
from turtle import settiltangle
from rest_api.views import *
#from debugapp import views

#para agregar nuevas path de url hay que agregar una coma al diccionario urlpatterns y seguir el formato descrito
urlpatterns = [
    path('index/', index,name="index"),
    path('Contacto', Contacto, name="Contacto"),
    path('', iniciarsesion, name="iniciarsesion"),
    path('productos/', productos, name="productos"),
    path('Crearcuenta/', register, name="Crearcuenta"),
    
      path('EditarPerfil_copy/', profile, name="EditarPerfil_copy"),
      path('admin/', admin, name="admin"),
      path('users/count/', UsersCountView.as_view(), name='users_count'),
      path('1/last-login/', last_login_api, name='last_login_api'),


]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns +=[
        path('debug/', include(debug_toolbar.urls)),
    ]