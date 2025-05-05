from django.urls import path, include
from gestao import views

urlpatterns = [
    path('laboratorios', views.laboratorio_list, name='laboratorio_list'),
    path('linhagens', views.laboratorio_list, name='laboratorio_list'),
    path('criar-laboratorio', views.laboratorio_create, name='laboratorio_create'),
    # path('editar-laboratorio/<int:pk>', views.laboratorio_update, name='laboratorio_update'),
    # path('deletar-laboratorio/<int:pk>', views.laboratorio_delete, name='laboratorio_delete'),

    path('projetos', views.projeto_list, name='projeto_list'),
    path('criar-projeto', views.projeto_create, name='projeto_create'),

    path('especies', views.especie_list, name='especie_list'),
    path('criar-especie', views.especie_create, name='especie_create'),
    
    path('meus_materiais', views.material_biologico_proprio_list, name='material_biologico_proprio_list'),
    path('materiais_compatilhados', views.material_biologico_compartilhados_list, name='material_biologico_compartilhados_list'),
    path('criar-material-biologico', views.material_biologico_create, name='material_biologico_create'),
    
]