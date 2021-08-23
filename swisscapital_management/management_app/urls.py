from django.urls import path
from . import views
from .api import api_view


urlpatterns = [
    path("", views.EmployeeList.as_view(), name="employee-list"),
    path(
        "detail-info/<int:pk>", views.EmployeeDetailView.as_view(), name="detail-info"
    ),
    path(
        "api/employee-list/", api_view.EmployeeList.as_view(), name="api-employee-list"
    ),
    path(
        "api/employee-retrieve/<int:pk>/",
        api_view.RetrieveEmployee.as_view(),
        name="api-retrieve-employee",
    ),
]
