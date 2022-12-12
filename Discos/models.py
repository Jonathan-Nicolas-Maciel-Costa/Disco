from wsgiref.handlers import format_date_time
from django.db import models
from datetime import datetime

# Create your models here.
"""
Nome;
Descrição;
Selo fonográfico;
Ano;
País;
Gênero;
Quantidade.
"""

class pais (models.Model):
    pais= models.CharField(("país"), max_length=50)
    
    class Meta:
        verbose_name = ("país")
        verbose_name_plural = ("países")
        
    def  __str__  (self):
        return self.pais.title()

class genero_musical (models.Model):
    genero = models.CharField(("genero"), max_length=50)
    
    class Meta:
        verbose_name = ("genero")
        verbose_name_plural = ("generos")
        
    def  __str__  (self):
        return self.genero.title()

class selo_fonografico (models.Model):
    selo_fonografico = models.CharField(("selo fonografico"), max_length=50)
    
    class Meta:
        verbose_name = ("selo fonografico")
        verbose_name_plural = ("selos fonograficos")
    
    def  __str__  (self):
        return self.selo_fonografico.title()

class disco (models.Model):

    nome = models.CharField(max_length=75, verbose_name='Nome')
    descricao = models.CharField(("Descrição"), max_length=250)
    selo_fonografico = models.ForeignKey(selo_fonografico, on_delete=models.CASCADE)
    ano = models.DateField( auto_now=False, auto_now_add=False)
    pais = models.ForeignKey(pais, on_delete=models.CASCADE)
    genero = models.ForeignKey(genero_musical, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    
    class Meta:
        verbose_name = ("Disco")
        verbose_name_plural = ("Discos")

    #anoo = ano[:3]
    #mes = ano[7:]
    #dia = ano[4:6]

    def __str__ (self):

        self.ano.strftime("%d/%m/%Y")
        return self.nome + ' (' + self.ano.strftime("%d/%m/%Y") +")"
