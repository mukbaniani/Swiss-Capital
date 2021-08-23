from rest_framework import viewsets, status
from .serializers import (
    DepartmentSerializer,
    EmployeeSerializer,
    PersonalQualitySerializer,
    RetrieveEmployeeSerializer,
    CreateEmployeeSerializer,
)
from ..models import Department, Employee, PersonalQuality
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class EmployeeView(viewsets.ViewSet):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

    def list(self, request):
        pagination = PageNumberPagination()
        employee_pagination = pagination.paginate_queryset(self.queryset, request)
        serializer = EmployeeSerializer(employee_pagination, many=True)
        return pagination.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        employee = get_object_or_404(self.queryset, pk=pk)
        serializer = RetrieveEmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        employee = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        employee = get_object_or_404(self.queryset, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PersonalQualityView(viewsets.ModelViewSet):
    queryset = PersonalQuality.objects.all()
    serializer_class = PersonalQualitySerializer
