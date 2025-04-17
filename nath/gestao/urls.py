from django.urls import path, include
from gestao import views

#BOTIJAO
urlpatterns = [
    path('laboratorios', views.laboratorio_list, name='laboratorio_list'),
    path('linhagens', views.laboratorio_list, name='laboratorio_list'),
    path('criar-laboratorio', views.laboratorio_create, name='laboratorio_create'),
    # path('editar-laboratorio/<int:pk>', views.laboratorio_update, name='laboratorio_update'),
    # path('deletar-laboratorio/<int:pk>', views.laboratorio_delete, name='laboratorio_delete'),

]