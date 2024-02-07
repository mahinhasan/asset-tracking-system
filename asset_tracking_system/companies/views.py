from django.shortcuts import render
from .models import Company,Employee
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework import generics



@login_required
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'companies/company_list.html', {'companies': companies})

@login_required
def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'companies/company_detail.html', {'company': company})

@login_required
def employee_list(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    employees = company.employees.all()
    return render(request, 'companies/employee_list.html', {'company': company, 'employees': employees})

@login_required
def employee_detail(request, company_id, employee_id):
    company = get_object_or_404(Company, pk=company_id)
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'companies/employee_detail.html', {'company': company, 'employee': employee})


# API

class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
