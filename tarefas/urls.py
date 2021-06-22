from django.urls import path

from tarefas.views import ListaView, CreateTarefasView, UpdateTarefasView, DeleteTarefasView

urlpatterns = [
    path('listatarefas/', ListaView.as_view(), name='listatarefas'),
    path('addt/', CreateTarefasView.as_view(), name='addt_tarefas'),
    path('<int:pk>/updatet/', UpdateTarefasView.as_view(), name='upd_tarefas'),
    path('<int:pk>/deletet/', DeleteTarefasView.as_view(), name='del_tarefas'),

]