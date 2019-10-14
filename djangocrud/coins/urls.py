from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inserir', views.inserir),
    path('deletar/<int:id>', views.deletar),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update)
]