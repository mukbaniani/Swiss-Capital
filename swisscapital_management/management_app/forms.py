from django import forms
from .models import Department, Employee, PersonalQuality


class EmployeeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    date_expiry = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    date_of_issue = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Employee
        fields = "__all__"


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class PersonalQaulityForm(forms.ModelForm):
    class Meta:
        model = PersonalQuality
        fields = "__all__"
