
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout_list, name='checkout_list'),
    path('<int:checkout_id>/', views.checkout_detail, name='checkout_detail'),
    path('create/', views.checkout_create, name='checkout_create'),
    path('<int:checkout_id>/update/', views.checkout_update, name='checkout_update'),
]
