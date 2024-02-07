
from django.urls import path
from . import views
from .views import CompanyListCreateAPIView, EmployeeListCreateAPIView


urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('<int:company_id>/', views.company_detail, name='company_detail'),
    path('<int:company_id>/employees/', views.employee_list, name='employee_list'),
    path('<int:company_id>/employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    #api
    path('api/create', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('api/employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
]
