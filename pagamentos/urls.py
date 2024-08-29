from django.urls import path
from pagamentos import views

urlpatterns =[
    path('processar/', views.ProcessarPagamentoFormView.as_view(),
         name='processar'),
    path('realizado/', views.PagRealizado.as_view(),
         name='pagrealizado'),
    path('cancelado/', views.PagCancelado.as_view(),
         name='pagcancelado'),
]