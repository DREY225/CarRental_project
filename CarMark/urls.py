from django.urls import path
from .views import carmark_list, carmark_detail, carmark_add, carmark_edit, carmark_delete

app_name = 'CarMark'

urlpatterns = [
    path('list_mark/', carmark_list, name='carmark_list'),
    path('<int:pk>/', carmark_detail, name='carmark_detail'),
    path('add/', carmark_add, name='carmark_add'),
    path('<int:pk>/edit/', carmark_edit, name='carmark_edit'),
    path('<int:pk>/delete/', carmark_delete, name='carmark_delete'),
]
