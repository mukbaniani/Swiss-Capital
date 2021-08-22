from rest_framework import serializers
from ..models import Department, Employee, PersonalQuality


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


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class PersonalQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalQuality
        fields = "__all__"
