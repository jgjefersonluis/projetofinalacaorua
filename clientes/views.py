from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from clientes.models import Clientes


class ListaClientesView(ListView):
    models = Clientes
    template_name = 'list.html'
    paginate_by = 5
    ordering = 'id'
    queryset = Clientes.objects.all().order_by()
    context_object_name = 'clientes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Clientes.objects.filter(
                Q(nome__icontains=query) |
                Q(idade__icontains=query) |
                Q(genero__icontains=query) |
                Q(etnia__icontains=query) |
                Q(spa__icontains=query) |
                Q(temporua__icontains=query)
            )
        else:
            return Clientes.objects.all()


class CreateClientesView(CreateView):
    model = Clientes
    template_name = 'clientes_form.html'
    fields = ['nome', 'aniversario', 'idade', 'cpf', 'escolaridade', 'genero', 'etnia', 'natural', 'spa', 'beneficios',
              'temporua', 'datacadastro', 'profissional']
    success_url = reverse_lazy('list')


class UpdateClientesView(UpdateView):
    model = Clientes
    template_name = 'clientes_form.html'
    fields = ['nome', 'aniversario', 'idade', 'cpf', 'escolaridade', 'genero', 'etnia', 'natural', 'spa', 'beneficios',
              'temporua', 'datacadastro', 'profissional']
    success_url = reverse_lazy('list')


class DeleteClientesView(DeleteView):
    model = Clientes
    template_name = 'clientes_del.html'
    success_url = reverse_lazy('list')
