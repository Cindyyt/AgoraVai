from django.db import models
#from stdimage.models import StdImageField

class Categoria(models.Model):
    nome = models.CharField('nome', max_length=45)
    informacoes = models.TextField('informacoes')
    ordem_menu = models.PositiveSmallIntegerField('ordem_menu', null=False, default=0)
    foto_categoria = models.ImageField(null=True, blank=True, upload_to='categorias')
    foto_topo = models.ImageField(null=True, blank=True, upload_to='categorias')
    #foto_categoria = models.ImageField(null=True, blank=True, upload_to='categorias/%Y/%m/%d')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Subcategoria(models.Model):
      categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True)

      nome = models.CharField(max_length=45)

      class Meta:
          verbose_name = 'Subcategoria'
          verbose_name_plural = 'Subcategorias'
          ordering = ['nome']

      def __str__(self):
          return self.nome

class Fornecedor(models.Model):
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, null= True)
    nome = models.CharField('nome', max_length=45)
    endereco = models.CharField('endereco',max_length=255, blank = True)
    contato= models.CharField('contato', max_length=45, null=True)
    informacoes = models.TextField(blank = True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['nome']

    def __str__(self):
        return self.nome



"""
EDUCACAO  (Categoria)

   > AULAS PARTICULARES MATEMATICA   (Subcategoria)
        > Douglas Maioli  (Fornecedor)

   > AULAS PARTICULARES INGLES
"""