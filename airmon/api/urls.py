from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

router = DefaultRouter()
router.register(r'captures', views.CaptureViewSet)
router.register(r'player/(?P<username>\w+)/captures', views.PlayerCaptureViewSet, basename="player-captures")
router.register(r'airmons', views.AirmonsViewSet)
router.register(r'players', views.PlayerViewSet, basename="endpoint1")

router.APIRootView.authentication_classes = [TokenAuthentication]
router.APIRootView.permission_classes = [IsAuthenticated]

urlpatterns = [
    path("", include(router.urls)),
    path("get-airmon-map/", views.AirmonOnMapView.as_view(), name="get-airmon-map"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("get-user/", views.get_current_user, name="get-user"),
    path("station/<str:code>/", views.StationViewSet.as_view({'get': 'retrieve'}), name="get-station"),
    path("map/", views.MapViewSet.as_view({'get': 'list'}), name="map"),
    # path("test-token/", views.test_token, name="test-token"),
    # path("endpoint1/", views.Endpoint1View.as_view(), name="endpoint1"),
    # path("endpoint2/", views.Endpoint2View.as_view(), name="endpoint2"),
    # Define more URL patterns as needed
]
