from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('clientes.urls')),
    path('', include('servicos.urls')),
    path('', include('diario.urls')),
    path('', include('tarefas.urls')),
    path('', include('graficos.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
