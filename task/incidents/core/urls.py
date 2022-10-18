from django.urls import path

from core.api import IncidentByDateAPI, IncidentAPI

urlpatterns = [
    path(f"by_date/", IncidentByDateAPI.as_view(), name="incident-by-date-api"),
    path(f"", IncidentAPI.as_view(), name="incident-api"),
    path(f"<int:pk>/", IncidentAPI.as_view(), name="incident-update-or-delete-api"),
]