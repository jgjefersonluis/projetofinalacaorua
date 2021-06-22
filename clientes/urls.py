from django.urls import path
from .views import ListaClientesView, CreateClientesView, UpdateClientesView, DeleteClientesView

urlpatterns = [
    path('list/', ListaClientesView.as_view(), name='list'),
    path('addc/', CreateClientesView.as_view(), name='add_clientes'),
    path('<int:pk>/updatec/', UpdateClientesView.as_view(), name='upd_clientes'),
    path('<int:pk>/deletec/', DeleteClientesView.as_view(), name='del_clientes'),

]