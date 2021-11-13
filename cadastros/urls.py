from django.urls import path

from .views import CadastrosView, CategoriaList, CategoriaCreate, CategoriaEdit, CategoriaDelete
from .views import SubcategoriaList, SubcategoriaCreate, SubcategoriaEdit, SubcategoriaDelete
from .views import FornecedorList, FornecedorCreate, FornecedorEdit, FornecedorDelete

app_name = 'cad_menu'

urlpatterns = [
    path('', CadastrosView.as_view(), name='cad_menu'),
    path('categorias', CategoriaList.as_view(), name='categoria_list'),
    path('categorias/<int:pk>/', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/<int:pk>/delete/', CategoriaDelete.as_view(), name='categoria_delete'),
    path('categorias/insert/', CategoriaCreate.as_view(), name='categoria_create'),
    path('subcategorias',SubcategoriaList.as_view(), name='subcategoria_list'),
    path('subcategorias/<int:pk>/', SubcategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/<int:pk>/delete/', SubcategoriaDelete.as_view(), name='subcategoria_delete'),
    path('subcategorias/insert/', SubcategoriaCreate.as_view(), name='subcategoria_create'),
    path('fornecedores',FornecedorList.as_view(), name='fornecedor_list'),
    path('fornecedores/<int:pk>/', FornecedorEdit.as_view(), name='fornecedor_edit'),
    path('fornecedores/<int:pk>/delete/', FornecedorDelete.as_view(), name='fornecedor_delete'),
    path('fornecedores/insert/', FornecedorCreate.as_view(), name='fornecedor_create'),
]
