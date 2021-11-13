from cadastros.models import Categoria

def get_menubar():
    return Categoria.objects.all().exclude(ordem_menu=0).order_by('ordem_menu')[:9]
