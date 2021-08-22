from django.views.generic.edit import UpdateView
from .models import Department, Employee, PersonalQuality
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .forms import DepartmentForm, EmployeeForm, PersonalQaulityForm
from django.urls import reverse_lazy


class EmployeeList(ListView):
    queryset = Employee.objects.only("first_name", "last_name", "person_number")
    template_name = "management_app/employeeList.html"
    context_object_name = "employees"
    paginate_by = 5


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "management_app/employeeDetailView.html"
    context_object_name = "employee"


class CreateEmployee(CreateView):
    model = Employee
    template_name = "management_app/create-employee.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employee-list")


class UpdateEmployee(UpdateView):
    model = Employee
    template_name = "management_app/update-employee.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("employee-list")


class DeleteEmployee(DeleteView):
    model = Employee
    template_name = "management_app/delete.html"
    success_url = reverse_lazy("employee-list")


class DepartmentList(ListView):
    model = Department
    template_name = "management_app/department-list.html"
    context_object_name = "departments"
    paginate_by = 5


class CreateDepartment(CreateView):
    model = Department
    template_name = "management_app/create-department.html"
    form_class = DepartmentForm
    success_url = reverse_lazy("department-list")


class UpdateDepartment(UpdateView):
    model = Department
    template_name = "management_app/update-department.html"
    form_class = DepartmentForm
    success_url = reverse_lazy("department-list")


class DeleteDepartment(DeleteView):
    model = Department
    template_name = "management_app/delete.html"
    success_url = reverse_lazy("department-list")


class PersonalQualityList(ListView):
    model = PersonalQuality
    template_name = "management_app/persona-quality-list.html"
    context_object_name = "personal_qualities"
    paginate_by = 5


class CreatePersonalQuality(CreateView):
    model = PersonalQuality
    template_name = "management_app/create-personal-quality.html"
    form_class = PersonalQaulityForm
    success_url = reverse_lazy("quality-list")


class UpdatePersonalQuality(UpdateView):
    model = PersonalQuality
    template_name = "management_app/update-personal-quality.html"
    form_class = PersonalQaulityForm
    success_url = reverse_lazy("quality-list")


class DeletePersonalQuality(DeleteView):
    model = PersonalQuality
    template_name = "management_app/delete.html"
    success_url = reverse_lazy("quality-list")
