from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.views import EntradaEmocaoViewSet, SessaoViewSet
from . import views

router = DefaultRouter()
router.register('entradas-emocao', EntradaEmocaoViewSet, basename='entrada-emocao')
router.register('sessoes', SessaoViewSet, basename='sessao')

urlpatterns = [
    path('api/', include(router.urls)),
     path('entrada-emocao/', views.page_entrada_emocao, name='entrada_emocao'),
    path('', views.home, name='home'),
]
