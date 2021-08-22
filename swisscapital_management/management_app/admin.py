from django.contrib import admin
from .models import Employee, Department, PersonalQuality


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "person_number"]
    list_filter = ["department_id"]
    search_fields = ["first_name", "last_name"]
    list_per_page = 5


admin.site.register([Department, PersonalQuality])
