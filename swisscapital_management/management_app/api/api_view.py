from rest_framework import generics
from .serializers import EmployeeSerializer, RetrieveEmployeeSerializer
from ..models import Employee


class EmployeeList(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.only("first_name", "last_name", "person_number")


class RetrieveEmployee(generics.RetrieveAPIView):
    serializer_class = RetrieveEmployeeSerializer
    queryset = Employee.objects.all()
