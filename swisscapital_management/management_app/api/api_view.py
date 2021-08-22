from rest_framework import generics, viewsets
from .serializers import (
    DepartmentSerializer,
    EmployeeSerializer,
    PersonalQualitySerializer,
    RetrieveEmployeeSerializer,
)
from ..models import Department, Employee, PersonalQuality


class EmployeeList(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.only("first_name", "last_name", "person_number")


class RetrieveEmployee(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RetrieveEmployeeSerializer
    queryset = Employee.objects.all()


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PersonalQualityView(viewsets.ModelViewSet):
    queryset = PersonalQuality.objects.all()
    serializer_class = PersonalQualitySerializer
