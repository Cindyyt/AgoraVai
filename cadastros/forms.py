from django import forms

from .models import Categoria, Subcategoria, Fornecedor

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('nome', 'informacoes', 'ordem_menu', 'foto_categoria', 'foto_topo', )

class SubcategoriaForm(forms.ModelForm):

    class Meta:
        model = Subcategoria
        fields = ('nome', 'categoria', )

class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = ('nome', 'subcategoria', 'endereco', 'contato', 'informacoes', )
