from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

router = DefaultRouter()
router.register(r'captures', views.CaptureViewSet)
router.register(r'player/(?P<username>\w+)/captures', views.PlayerCaptureViewSet, basename="player-captures")
router.register(r'airmons', views.AirmonsViewSet)
router.register(r'images', views.PlayerImageViewSet, basename="images")
router.register(r'items', views.ItemViewSet, basename="items")

router.register(r'player/items', views.PlayerItemViewSet, basename="player-items")
router.register(r'player/active-items', views.PlayerActiveItemViewSet, basename="active-items")


router.APIRootView.authentication_classes = [TokenAuthentication]
router.APIRootView.permission_classes = [IsAuthenticated]

urlpatterns = [
    path("", include(router.urls)),
    path("get-airmon-map/", views.AirmonOnMapView.as_view(), name="get-airmon-map"),
    path("spawned_airmons/", views.SpawnedAirmonsView.as_view(), name="spawned_airmons"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("get-user/", views.get_current_user, name="get-user"),
    path("icqa/", views.ICQAView.as_view(), name="get-icqa"),
    path('find-user/<str:key>/', views.FindUserViewSet.as_view({"get": "list"}), name="find-user"),
    path("station/<str:code>/", views.StationViewSet.as_view({'get': 'retrieve'}), name="get-station"),
    path("map/", views.MapViewSet.as_view({'get': 'list'}), name="map"),
    path("chat/", views.ChatView.as_view(), name="chat"),
    path('stations/', views.StationViewSet.as_view({'get': 'list'}), name="stations"),
    path("posts/<str:username>/", views.PlayerImageView.as_view({"get": "retrieve"})),
    path("chat/<int:chat_id>", views.ChatView.as_view(), name="chat"),
    path("friendship/", views.FriendshipViewSet.as_view({'post': 'create', 'get': 'retrieve', 'delete': 'delete'}),
         name="friendship"),
    path('player/<str:username>/', views.PlayerViewSet.as_view({'get': 'retrieve'}), name="player"),
    path('player/roulette', views.RouletteView.as_view({'post': 'create', 'get': 'retrieve'}), name='roulette'),
    path('players/', views.PlayerViewSet.as_view({'get': 'list'}), name="players"),
    path("edit-user/", views.EditUserViewSet.as_view({'post': 'update'}), name="edit-profile"),
    path('trophy/<str:name>/', views.TrophyViewSet.as_view({'get': 'retrieve'}), name="throphy"),
    # path("test-token/", views.test_token, name="test-token"),
    # path("endpoint1/", views.Endpoint1View.as_view(), name="endpoint1"),
    # path("endpoint2/", views.Endpoint2View.as_view(), name="endpoint2"),
    # Define more URL patterns as needed
]
