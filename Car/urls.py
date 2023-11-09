from django.urls import path
from .views import car_list, car_detail, car_add, car_edit, car_delete

app_name = 'Car'

urlpatterns = [
    path('list/', car_list, name='car_list'),
    path('<int:pk>/', car_detail, name='car_detail'),
    path('add/', car_add, name='car_add'),
    path('<int:pk>/edit/', car_edit, name='car_edit'),
    path('<int:pk>/delete/', car_delete, name='car_delete'),
]
