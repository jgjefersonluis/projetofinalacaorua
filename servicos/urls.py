from django.urls import path
from .views import ListaView, CreateServicosView, UpdateServicosView, DeleteServicosView

urlpatterns = [
    path('listaservicos/', ListaView.as_view(), name='listaservicos'),
    path('adds/', CreateServicosView.as_view(), name='adds_servicos'),
    path('<int:pk>/updates/', UpdateServicosView.as_view(), name='upd_servicos'),
    path('<int:pk>/deletes/', DeleteServicosView.as_view(), name='del_servicos'),

]