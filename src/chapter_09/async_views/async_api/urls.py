from django.urls import path

from .views import requests_view, requests_view_sync

app_name = "async_api"

urlpatterns = [
    path("", requests_view, name=app_name),
    path('async_to_sync', requests_view_sync),
]
