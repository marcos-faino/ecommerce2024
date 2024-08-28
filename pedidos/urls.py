from django.urls import path
from pedidos import views

urlpatterns = [
    path('add/', views.PedidoCreateView.as_view(), name='addpedido'),
    path('resumo/pedido/<int:idpedido>', views.ResumoPedidoTemplateView.as_view(),
         name='resumopedido'),
    path('meuspedidos/', views.PedidosListView.as_view(), name='meuspedidos'),
]