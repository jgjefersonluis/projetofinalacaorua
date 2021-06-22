from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from diario.models import Diario


class ListaView(ListView):
    models = Diario
    template_name = 'listadiario.html'
    paginate_by = 5
    ordering = 'id'
    queryset = Diario.objects.all().order_by()
    context_object_name = 'diario'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Diario.objects.filter(
                Q(profissional__icontains=query) |
                Q(acao__icontains=query)
            )
        else:
            return Diario.objects.all()


class CreateDiarioView(CreateView):
    model = Diario
    template_name = 'diario_form.html'
    fields = ['data', 'hora', 'local', 'profissional', 'acao', 'sujeitos', 'avaliacao']
    success_url = reverse_lazy('listadiario')


class UpdateDiarioView(UpdateView):
    model = Diario
    template_name = 'diario_form.html'
    fields = ['data', 'hora', 'local', 'profissional', 'acao', 'sujeitos', 'avaliacao']
    success_url = reverse_lazy('listadiario')


class DeleteDiarioView(DeleteView):
    model = Diario
    template_name = 'diario_del.html'
    success_url = reverse_lazy('listadiario')
