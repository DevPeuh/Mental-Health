from django import forms
from .models import Entrada_Emocao

class EntradaEmocaoForm(forms.ModelForm):
    class Meta:
        model = Entrada_Emocao
        fields = ['emocao', 'anotacao'  ]