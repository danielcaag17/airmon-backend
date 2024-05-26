from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

router = DefaultRouter()
router.register(r'airmons', views.AirmonsViewSet)
router.register(r'images', views.PlayerImageViewSet, basename='images')
router.register(r'items', views.ItemViewSet, basename='items')
router.register(r'captures', views.CaptureViewSet)
router.register(r'player/captures', views.PlayerCaptureViewSet, basename='player-captures')
router.register(r'player/active-items', views.PlayerActiveItemViewSet, basename='active-items')
router.register(r'player/items', views.PlayerItemViewSet, basename='player-items')

router.APIRootView.authentication_classes = [TokenAuthentication]
router.APIRootView.permission_classes = [IsAuthenticated]

airmon_urls = [
    path('get-airmon-map/', views.AirmonOnMapView.as_view(), name='get-airmon-map'),
    path('spawned_airmons/', views.SpawnedAirmonsView.as_view(), name='spawned_airmons'),
]

event_urls = [
    path('events/', views.EventViewSet.as_view({'get': 'list'}), name='events'),
    # path('event/', views.run_script_view, name='event'),
]

user_urls = [
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('chat/<int:chat_id>', views.ChatView.as_view(), name='chat'),
    path('edit-user/', views.EditUserViewSet.as_view({'post': 'update'}), name='edit-profile'),
    path('find-user/<str:key>/', views.FindUserViewSet.as_view({'get': 'list'}), name='find-user'),
    path('friendship/', views.FriendshipViewSet.as_view({'post': 'create', 'get': 'retrieve', 'delete': 'delete'}),
         name='friendship'),
    path('get-user/', views.get_current_user, name='get-user'),
    path('login/', views.login, name='login'),
    path('posts/<str:username>/', views.PlayerImageView.as_view({'get': 'retrieve'}), name='player-images'),
    path('register/', views.register, name='register'),
]

player_urls = [
    path('edit-user/', views.EditUserViewSet.as_view({'post': 'update'}), name='edit-profile'),
    path('player/exp/', views.ExpView.as_view({'get': 'retrieve', 'put': 'partial_update'}), name='exp'),
    path('player/coins/', views.PlayerViewSet.as_view({'post': 'update'}), name='coins'),
    path('player/roulette/', views.RouletteView.as_view({'post': 'create', 'get': 'retrieve'}), name='roulette'),
    path('player/<str:username>/', views.PlayerViewSet.as_view({'get': 'retrieve'}), name='player'),
    path('players/', views.PlayerViewSet.as_view({'get': 'list'}), name='players'),
    path('players/statistics/<str:statistic>/', views.RankingViewSet.as_view({'get': 'list'}), name='player-ranking'),
    path('<str:username>/statistics/', views.PlayerStatisticsViewSet.as_view({'get': 'list'}), name='statistics'),
]

station_urls = [
    path('icqa/', views.ICQAView.as_view(), name='get-icqa'),
    path('map/', views.MapViewSet.as_view({'get': 'list'}), name='map'),
    path('station/<str:code>/', views.StationViewSet.as_view({'get': 'retrieve'}), name='get-station'),
    path('stations/', views.StationViewSet.as_view({'get': 'list'}), name='stations'),
]

trophies_urls = [
    path("trophies/<str:username>/", views.PlayerTrophyViewSet.as_view({'get': 'list'}), name="trophies-player"),
    path('trophy/<str:name>/', views.TrophyViewSet.as_view({'get': 'retrieve'}), name="throphy"),
]

urlpatterns = [
    path('', include(router.urls)),
    # path('test-token/', views.test_token, name='test-token'),
] + airmon_urls + event_urls + user_urls + player_urls + station_urls + trophies_urls
