from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Producto, Comentario
from .forms import ActualizacionProducto, FormularioCambioPassword, FormularioEdicion, FormularioNuevoProducto, FormularioRegistroUsuario, FormularioComentario


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'Base/home.html'

class LoginPagina(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'base/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'base/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'base/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'base/passwordExitoso.html', {})


# CASCO

class CascoLista(LoginRequiredMixin, ListView):
    context_object_name = 'cascos'
    queryset = Producto.objects.filter(producto__startswith='casco')
    template_name = 'Base/listaCascos.html'
    login_url = '/login/'

class CascoDetalle(LoginRequiredMixin, DetailView):
    model = Producto
    context_object_name = 'casco'
    template_name = 'Base/cascoDetalle.html'

class CascoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ActualizacionProducto
    success_url = reverse_lazy('cascos')
    context_object_name = 'casco'
    template_name = 'Base/cascoEdicion.html'

class CascoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('cascos')
    context_object_name = 'casco'
    template_name = 'Base/cascoBorrado.html'

# ACCESORIOS

class AccesoriosLista(LoginRequiredMixin, ListView):
    context_object_name = 'accesorios'
    queryset = Producto.objects.filter(producto__startswith='accesorios')
    template_name = 'Base/listaAccesorios.html'

class AccesoriosDetalle(LoginRequiredMixin,DetailView):
    model = Producto
    context_object_name = 'accesorios'
    template_name = 'Base/accesoriosDetalle.html'

class AccesoriosUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ActualizacionProducto
    success_url = reverse_lazy('accesorios')
    context_object_name = 'accesorios'
    template_name = 'Base/accesoriosEdicion.html'

class AccesoriosDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('accesorios')
    context_object_name = 'accesorios'
    template_name = 'Base/accesoriosBorrado.html'

# INDUMENTARIA

class IndumentariaLista(LoginRequiredMixin, ListView):
    context_object_name = 'Indumentaria'
    queryset = Producto.objects.filter(producto__startswith='indumentaria')
    template_name = 'Base/listaIndumentaria.html'

class IndumentariaDetalle(LoginRequiredMixin, DetailView):
    model = Producto
    context_object_name = 'indumentaria'
    template_name = 'Base/indumentariaDetalle.html'

class IndumentariaUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ActualizacionProducto
    success_url = reverse_lazy('Indumentaria')
    context_object_name = 'indumentaria'
    template_name = 'Base/indumentariaEdicion.html'

class IndumentariaDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('Indumentaria')
    context_object_name = 'indumentaria'
    template_name = 'Base/indumentariaBorrado.html'

# MOTOS

class MotosLista(LoginRequiredMixin, ListView):
    context_object_name = 'motos'
    queryset = Producto.objects.filter(producto__startswith='motos')
    template_name = 'Base/listaMotos.html'

class MotosDetalle(LoginRequiredMixin, DetailView):
    model = Producto
    context_object_name = 'motos'
    template_name = 'Base/motosDetalle.html'

class MotosUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ActualizacionProducto
    success_url = reverse_lazy('motos')
    context_object_name = 'motos'
    template_name = 'Base/motosEdicion.html'

class MotosDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('motos')
    context_object_name = 'motos'
    template_name = 'Base/motosBorrado.html'


# OTRO

class OtroLista(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = Producto.objects.filter(producto__startswith='otro')
    template_name = 'Base/listaOtros.html'

class OtroDetalle(LoginRequiredMixin, DetailView):
    model = Producto
    context_object_name = 'otro'
    template_name = 'Base/otroDetalle.html'

class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ActualizacionProducto
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'Base/otroEdicion.html'

class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'Base/otroBorrado.html'

# CREACION PRODUCTO

class ProductoCreacion(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = FormularioNuevoProducto
    success_url = reverse_lazy('home')
    template_name = 'Base/productoCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductoCreacion, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'Base/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'base/acercaDeMi.html', {})


