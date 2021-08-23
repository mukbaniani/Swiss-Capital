from rest_framework import serializers
from ..models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "first_name", "last_name", "person_number"]


class RetrieveEmployeeSerializer(serializers.ModelSerializer):
    department_id = serializers.SlugRelatedField(
        slug_field="department_name", read_only=True
    )

    class Meta:
        model = Employee
        fields = "__all__"
        depth = 1
