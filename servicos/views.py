from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from servicos.models import Servicos


class ListaView(ListView):
    models = Servicos
    template_name = 'listaservicos.html'
    paginate_by = 5
    ordering = 'id'
    queryset = Servicos.objects.all()
    context_object_name = 'servicos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Servicos.objects.filter(
                Q(nome__icontains=query) |
                Q(acao__icontains=query)
            )
        else:
            return Servicos.objects.all()


class CreateServicosView(CreateView):
    model = Servicos
    template_name = 'servicos_form.html'
    fields = ['data', 'turno', 'profissional', 'nome', 'acao', 'demanda', 'encaminhamento', 'logradouro', 'observacoes']
    success_url = reverse_lazy('listaservicos')


class UpdateServicosView(UpdateView):
    model = Servicos
    template_name = 'servicos_form.html'
    fields = ['data', 'turno', 'profissional', 'nome', 'acao', 'demanda', 'encaminhamento', 'logradouro', 'observacoes']
    success_url = reverse_lazy('listaservicos')


class DeleteServicosView(DeleteView):
    model = Servicos
    template_name = 'servicos_del.html'
    success_url = reverse_lazy('listaservicos')
