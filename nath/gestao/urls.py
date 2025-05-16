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
    
    path('minhas-amostras', views.amostra_list, name='amostra_list'),
    path('criar-amostra', views.amostra_create, name='amostra_create'),
    path('ver-amostra/<int:pk>', views.amostra_read, name='amostra_read'),
    path('alterar-amostra/<int:pk>', views.amostra_update, name='amostra_update'),
    path('solicitar-amostra/<int:pk>', views.amostra_solicitar, name='amostra_solicitar'),
    path('alterar-compartilhamento-amostra/<int:pk>', views.amostra_share_toogle, name='amostra_share_toogle'),
    
    path('amostras-compatilhadas', views.amostra_compartilhada_list, name='amostra_compartilhada_list'),
    path('ver-amostra-compatilhada/<int:pk>', views.amostra_compartilhada_read, name='amostra_compartilhada_read'),
    
    path('minhas-solicitacoes', views.minhas_solicitacoes_list, name='minhas_solicitacoes_list'),
    path('atender-solicitacao/<int:pk>', views.atender_solicitacao, name='atender_solicitacao'),
     
]