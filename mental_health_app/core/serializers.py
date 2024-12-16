from rest_framework import serializers
from .models import Sessao, Entrada_Emocao

class Serializar_Entrada_Emocao(serializers.ModelSerializer):
    class Meta:
        model = Entrada_Emocao
        fields = '__all__'

class Serializar_sessao(serializers.ModelSerializer):
    class Meta:
        model = Sessao
        fields = '__all__'