from django import views
from django.urls import path
from .views import CascoDelete, ProductoCreacion, CascoDetalle, MotosLista, AccesoriosLista, CascoLista, IndumentariaLista, OtroLista, AccesoriosDetalle, IndumentariaDetalle, MotosDetalle, OtroDetalle, CascoUpdate, AccesoriosUpdate, IndumentariaUpdate, MotosUpdate, OtroUpdate, AccesoriosDelete, IndumentariaDelete, MotosDelete, OtroDelete, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView, ComentarioPagina
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaCascos/', CascoLista.as_view(), name='cascos'),
    path('listaAccesorios/', AccesoriosLista.as_view(), name='accesorios'),
    path('listaIndumentaria/', IndumentariaLista.as_view(), name='Indumentaria'),
    path('listaMotos/', MotosLista.as_view(), name='motos'),
    path('listaOtros/', OtroLista.as_view(), name='otros'),

    path('cascoDetalle/<int:pk>/', CascoDetalle.as_view(), name='casco'),
    path('accesoriosDetalle/<int:pk>/', AccesoriosDetalle.as_view(), name='accesorios'),
    path('indumentariaDetalle/<int:pk>/', IndumentariaDetalle.as_view(), name='indumentaria'),
    path('motosDetalle/<int:pk>/', MotosDetalle.as_view(), name='motos'),
    path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),

    path('cascoEdicion/<int:pk>/', CascoUpdate.as_view(), name='casco_editar'),
    path('accesoriosEdicion/<int:pk>/', AccesoriosUpdate.as_view(), name='accesorios_editar'),
    path('indumentariaEdicion/<int:pk>/', IndumentariaUpdate.as_view(), name='indumentaria_editar'),
    path('motosEdicion/<int:pk>/', MotosUpdate.as_view(), name='motos_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),


    path('cascoBorrado/<int:pk>/', CascoDelete.as_view(), name='casco_eliminar'),
    path('accesoriosBorrado/<int:pk>/', AccesoriosDelete.as_view(), name='accesorios_eliminar'),
    path('indumentariaBorrado/<int:pk>/', IndumentariaDelete.as_view(), name='indumentaria_eliminar'),
    path('motosBorrado/<int:pk>/', MotosDelete.as_view(), name='motos_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('productoCreacion/', ProductoCreacion.as_view(), name='nuevo'),

    path('cascoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('accesoriosDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('indumentariaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('motosDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]
