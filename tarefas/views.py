from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView

from tarefas.models import Tarefas


class ListaView(ListView):
    models = Tarefas
    template_name = 'listatarefas.html'
    paginate_by = 5
    ordering = 'id'
    queryset = Tarefas.objects.all()
    context_object_name = 'tarefas'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Tarefas.objects.filter(
                Q(titulo__icontains=query) |
                Q(descricao__icontains=query)|
                Q(status__icontains=query)
            )
        else:
            return Tarefas.objects.all()


class CreateTarefasView(CreateView):
    model = Tarefas
    template_name = 'tarefas_form.html'
    fields = ['titulo', 'descricao', 'status']
    success_url = reverse_lazy('listatarefas')


class UpdateTarefasView(UpdateView):
    model = Tarefas
    template_name = 'tarefas_form.html'
    fields = ['titulo', 'descricao', 'status']
    success_url = reverse_lazy('listatarefas')


class DeleteTarefasView(DeleteView):
    model = Tarefas
    template_name = 'tarefas_del.html'
    success_url = reverse_lazy('listatarefas')
