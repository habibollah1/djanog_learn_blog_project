from . import views
from django.urls import path

urlpatterns = [
    path('', views.kala_view_func, name='kala_list'),
    path('<int:pk>/', views.kala_types_func, name='types_of_kala'),
    path('create/', views.new_kala_func, name= 'new_kala_create'),
]
