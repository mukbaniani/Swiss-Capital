from .models import Employee
from django.views.generic import ListView, DetailView


class EmployeeList(ListView):
    queryset = Employee.objects.only("first_name", "last_name", "person_number")
    template_name = "management_app/employeeList.html"
    context_object_name = "employees"
    paginate_by = 5


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "management_app/employeeDetailView.html"
    context_object_name = "employee"
