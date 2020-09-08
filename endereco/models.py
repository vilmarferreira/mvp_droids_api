from django.db import models

# Create your models here.

class Estado(models.Model):
    nome = models.CharField(max_length=20)
    UF = models.CharField(max_length=2)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.UF


class Endereco(models.Model):
    rua = models.CharField(max_length= 100)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=20, blank=True)
    bairro = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    estado = models.ForeignKey('Estado',on_delete=models.PROTECT, related_name='endereco_estado')

    def __str__(self):
        return 'Rua:{0} ,Número:{1}, Complemento:{2}, Bairro:{3}, Cidade:{4} - {5}'.format(self.rua,self.numero,self.complemento, self.bairro, self.cidade, self.estado)