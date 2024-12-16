from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Sessao, Entrada_Emocao
from .serializers import Serializar_Entrada_Emocao, Serializar_sessao
from rest_framework.permissions import IsAuthenticated
from .forms import EntradaEmocaoForm
from django.contrib.auth.models import User


def home(request):
    return render(request, 'core/home.html')

def page_entrada_emocao(request):
    if request.method == "POST":
        form = EntradaEmocaoForm(request.POST)
        if form.is_valid():
            entrada_emocao = form.save(commit=False)
            if request.user.is_authenticated:
                entrada_emocao.usuario = request.user
            else:
                entrada_emocao.usuario = User.objects.get_or_create(username='anonimo')[0]  

            entrada_emocao.save()
            return redirect('entrada_emocao')
    else:
        form = EntradaEmocaoForm()

    entradas = Entrada_Emocao.objects.all()

    return render(request, 'core/entrada_emocao.html', {'form': form, 'entradas': entradas})

class EntradaEmocaoViewSet(viewsets.ModelViewSet): 
    queryset = Entrada_Emocao.objects.all() 
    serializer_class = Serializar_Entrada_Emocao  
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        return Entrada_Emocao.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class SessaoViewSet(viewsets.ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = Serializar_sessao
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sessao.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
