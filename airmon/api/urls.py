from django.urls import path
from . import views

urlpatterns = [
    path("endpoint1/", views.Endpoint1View.as_view(), name="endpoint1"),
    # path("endpoint2/", views.Endpoint2View.as_view(), name="endpoint2"),
    # Define more URL patterns as needed
]
