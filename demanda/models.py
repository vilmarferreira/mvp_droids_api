from django.db import models
from django.utils.html import format_html
# Create your models here.
STATUS_CHOICES = [
    ('A','Aberto'),
    ('F','Finalizado')
]
class Demanda(models.Model):
    descricao = models.CharField(max_length=100)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, default='A')
    endereco = models.ForeignKey('endereco.Endereco', on_delete=models.PROTECT, verbose_name='Endereço',related_name='demanda_endereço')
    contato = models.ForeignKey('contato.Contato',on_delete=models.PROTECT,verbose_name='Contato',related_name='demanda_contato')
    anunciante = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='demandas_anunciantes',verbose_name='Anunciante')

    def finalizado(self):
        a = '<img src="/static/icons/baseline-highlight_off.svg">'
        f = '<img src="/static/icons/baseline-check_circle_outline.svg" alt="True">'
        if self.status == 'A':
            return format_html(a)
        else:
            return format_html(f)
    def finalizar(self):
        self.status = 'F'
        self.save()