from django.urls import path

from graficos import views

urlpatterns = [
    path('beneficio/', views.beneficio, name='beneficio'),
    path('etnia/', views.etnia, name='etnia'),
    path('faixa-etaria/', views.faixaetaria, name='faixa-etaria'),
    path('genero/', views.genero, name='genero'),
    path('saude/', views.saude, name='saude'),
    path('substancias/', views.substancias, name='substancias'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('pie-chart1/', views.pie_chart1, name='pie-chart1'),
    path('pie-chart2/', views.pie_chart2, name='pie-chart2'),
    path('pie-chart3/', views.pie_chart3, name='pie-chart3'),
    path('pie-chart4/', views.pie_chart4, name='pie-chart4'),
    path('pie-chart5/', views.pie_chart5, name='pie-chart5'),

]
