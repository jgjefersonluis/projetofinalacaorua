from django.urls import path


from diario.views import ListaView, CreateDiarioView, UpdateDiarioView, DeleteDiarioView

urlpatterns = [
    path('listadiario/', ListaView.as_view(), name='listadiario'),
    path('addd/', CreateDiarioView.as_view(), name='addd_diario'),
    path('<int:pk>/updated/', UpdateDiarioView.as_view(), name='upd_diario'),
    path('<int:pk>/deleted/', DeleteDiarioView.as_view(), name='del_diario'),

    ]