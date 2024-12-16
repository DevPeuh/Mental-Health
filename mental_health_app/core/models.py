from django.db import models
from django.contrib.auth.models import User

class Entrada_Emocao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    emocao = models.CharField(max_length=250)
    data = models.DateField(auto_now_add=True)
    data_atualizada = models.DateTimeField(auto_now=True)
    anotacao = models.TextField(blank=True, null= True)

    def __str__(self):
        return f"{self.usuario} - {self.emocao} (Criação: {self.data})"

class Sessao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    terapeuta = models.CharField(max_length=250)
    data = models.DateField(auto_now_add=True)
    data_atualizada = models.DateTimeField(auto_now=True)
    anotacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario} - {self.emocao} (Criação: {self.data})"
