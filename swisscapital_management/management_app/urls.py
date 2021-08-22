from django.urls import path
from . import views
from .api import api_view
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(
    "api/department",
    api_view.DepartmentView,
    basename="department-view",
)

router.register(
    "api/personal-quality",
    api_view.PersonalQualityView,
    basename="personal-quality",
)

urlpatterns = [
    path("", views.EmployeeList.as_view(), name="employee-list"),
    path(
        "detail-info/<int:pk>", views.EmployeeDetailView.as_view(), name="detail-info"
    ),
    path("create-employee", views.CreateEmployee.as_view(), name="create-employee"),
    path(
        "delete-employee/<int:pk>",
        views.DeleteEmployee.as_view(),
        name="delete-employee",
    ),
    path(
        "update-employee/<int:pk>",
        views.UpdateEmployee.as_view(),
        name="update-employee",
    ),
    path("department-list", views.DepartmentList.as_view(), name="department-list"),
    path(
        "create-department", views.CreateDepartment.as_view(), name="create-department"
    ),
    path(
        "delete-department/<int:pk>",
        views.DeleteDepartment.as_view(),
        name="delete-department",
    ),
    path(
        "update-department/<int:pk>",
        views.UpdateDepartment.as_view(),
        name="update-department",
    ),
    path(
        "personal-quality-list",
        views.PersonalQualityList.as_view(),
        name="quality-list",
    ),
    path(
        "create-personal-quality",
        views.CreatePersonalQuality.as_view(),
        name="create-personal-quality",
    ),
    path(
        "delete-personal-quality/<int:pk>",
        views.DeletePersonalQuality.as_view(),
        name="delete-personal-quality",
    ),
    path(
        "update-personal-quality/<int:pk>",
        views.UpdatePersonalQuality.as_view(),
        name="update-personal-quality",
    ),
    path(
        "api/employee-list", api_view.EmployeeList.as_view(), name="api-employee-list"
    ),
    path(
        "api/employee-retrieve/<int:pk>",
        api_view.RetrieveEmployee.as_view(),
        name="api-retrieve-employee",
    ),
] + router.urls
