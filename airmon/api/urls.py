from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'map', views.MapViewSet, basename='map')

urlpatterns = router.urls + [
    path('map/', views.MapViewSet.as_view({'get': 'list'}), name='map'),
    # path('', include(router.urls)),
    # path("endpoint1/", views.Endpoint1View.as_view(), name="endpoint1"),
    # path("endpoint2/", views.Endpoint2View.as_view(), name="endpoint2"),
    # Define more URL patterns as needed
]
