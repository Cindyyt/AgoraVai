from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.http import Http404

from users.models  import User
from cadastros.models import Categoria, Subcategoria, Fornecedor
import services.categoria_service as CategoriaService

class HomePageView(ListView):

    paginate_by = 5
    context_object_name = 'db'
    CATEGORIA_DEFAULT_ID = 4

    def get_queryset(self):

        #self.template_name = 'home.html' if not self.kwargs.get('cat') else 'lista_fornecedor.html'
        #self.cat_pk = self.kwargs.get('cat') if self.kwargs.get('cat') else HomePageView.CATEGORIA_DEFAULT_ID

        self.sub_pk = self.kwargs.get('sub')

        if not self.kwargs.get('cat'):
            self.template_name = 'home.html'
            self.cat_pk = HomePageView.CATEGORIA_DEFAULT_ID
            self.is_home = True
        else:
            self.template_name = 'lista_fornecedor.html'
            self.cat_pk = self.kwargs.get('cat')
            self.is_home = False

        for i in range(2):
            cat_dict = Categoria.objects.filter(pk=self.cat_pk).values('nome', 'foto_topo')
            if len(cat_dict) != 0:
                self.cat_nome = cat_dict[0].get('nome')
                self.cat_foto = cat_dict[0].get('foto_topo')
                break
            self.cat_pk = HomePageView.CATEGORIA_DEFAULT_ID

        if not self.sub_pk:
            sub_dict = Subcategoria.objects.filter(categoria=self.cat_pk).values('id')
            if len(sub_dict) != 0:
                self.sub_pk = sub_dict[0].get('id')

        self.query_sub = Subcategoria.objects.filter(categoria=self.cat_pk)

        queryset = Fornecedor.objects.filter(subcategoria=self.sub_pk)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_db'] = self.query_sub
        context['sub_pk'] = self.sub_pk
        context['cat_db'] = CategoriaService.get_menubar()
        context['categoria_nome'] = self.cat_nome
        context['categoria_foto'] = self.cat_foto
        context['is_home'] = self.is_home

        return context
