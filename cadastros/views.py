from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from braces.views import GroupRequiredMixin

from .forms import CategoriaForm, SubcategoriaForm, FornecedorForm
from .models import Categoria, Subcategoria, Fornecedor
import services.categoria_service as CategoriaService

#class CadastrosView(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
class CadastrosView(LoginRequiredMixin, TemplateView):

    template_name = 'cadastros/index.html'
    #group_required = 'admin_users'  # se descomentar essas linhas
    #redirect_field_name = '/'       # essa tela nao tá aparecendo nem para admin

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context


# Categoria
# --------------------------

class CategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):

    model = Categoria
    form_class = CategoriaForm
    context_object_name = 'db'
    template_name = 'cadastros/categoria/list.html'
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context

class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    model = Categoria
    form_class = CategoriaForm
    template_name = 'cadastros/categoria/form.html'
    success_url = reverse_lazy('cadastros:categoria_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context

class CategoriaEdit(GroupRequiredMixin, LoginRequiredMixin, UpdateView):

    model = Categoria
    form_class = CategoriaForm
    template_name = 'cadastros/categoria/form.html'
    success_url = reverse_lazy('cadastros:categoria_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context

class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):

    model = Categoria
    template_name = 'cadastros/categoria/confirm_delete.html'
    success_url = reverse_lazy('cadastros:categoria_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context


# Subcategoria
# --------------------------

class SubcategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):

    model = Subcategoria
    form_class = SubcategoriaForm
    context_object_name = 'db'
    template_name = 'cadastros/subcategoria/list.html'
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context

class SubcategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    model = Subcategoria
    form_class = SubcategoriaForm
    template_name = 'cadastros/subcategoria/form.html'
    success_url = reverse_lazy('cadastros:subcategoria_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context

class SubcategoriaEdit(GroupRequiredMixin, LoginRequiredMixin, UpdateView):

    model = Subcategoria
    form_class = SubcategoriaForm
    template_name = 'cadastros/subcategoria/form.html'
    success_url = reverse_lazy('cadastros:subcategoria_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context

class SubcategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):

    model = Subcategoria
    template_name = 'cadastros/subcategoria/confirm_delete.html'
    success_url = reverse_lazy('cadastros:subcategoria_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context


# Fornecedor
# --------------------------

class FornecedorList(GroupRequiredMixin, LoginRequiredMixin, ListView):

    model = Fornecedor
    form_class = FornecedorForm
    context_object_name = 'db'
    template_name = 'cadastros/fornecedor/list.html'
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context

class FornecedorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):

    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'cadastros/fornecedor/form.html'
    success_url = reverse_lazy('cadastros:fornecedor_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context

class FornecedorEdit(GroupRequiredMixin, LoginRequiredMixin, UpdateView):

    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'cadastros/fornecedor/form.html'
    success_url = reverse_lazy('cadastros:fornecedor_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context

class FornecedorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):

    model = Fornecedor
    template_name = 'cadastros/fornecedor/confirm_delete.html'
    success_url = reverse_lazy('cadastros:fornecedor_list')
    group_required = 'admin_users'
    redirect_field_name = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_db'] = CategoriaService.get_menubar()
        return context
