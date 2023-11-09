from django.urls import path
from .views import carmodel_list, carmodel_detail, carmodel_add, carmodel_edit, carmodel_delete

app_name = 'CarModel'

urlpatterns = [
    path('list_model/', carmodel_list, name='carmodel_list'),
    path('<int:pk>/', carmodel_detail, name='carmodel_detail'),
    path('add/', carmodel_add, name='carmodel_add'),
    path('<int:pk>/edit/', carmodel_edit, name='carmodel_edit'),
    path('<int:pk>/delete/', carmodel_delete, name='carmodel_delete'),
]
