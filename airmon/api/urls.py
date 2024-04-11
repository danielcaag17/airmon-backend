from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'map', views.MapViewSet, basename='map')
router.register(r'captures', views.CaptureViewSet)
router.register(r'player/(?P<username>\w+)/captures', views.PlayerCaptureViewSet, basename="player-captures")
router.register(r'station/(?P<code>\w+)', views.StationViewSet, basename="station-measures")
router.register(r'airmons', views.AirmonsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("get-airmon-map/", views.AirmonOnMapView.as_view(), name="get-airmon-map"),
    # path("endpoint1/", views.Endpoint1View.as_view(), name="endpoint1"),
    # path("endpoint2/", views.Endpoint2View.as_view(), name="endpoint2"),
    # Define more URL patterns as needed
]
