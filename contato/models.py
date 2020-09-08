from django.db import models

# Create your models here.

class Contato(models.Model):
    celular = models.CharField(max_length=11)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return 'Celular: {0}, E-mail: {1}'.format(self.celular,self.email)

