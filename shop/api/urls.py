from django.urls import path
from . import views

urlpatterns = [
    path('add-wish/<int:pk>/', views.add_wish, name='api-add-wish'),
    path('remove-wish/<int:pk>/', views.remove_wish, name='api-remove-wish'),
]