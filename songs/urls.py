from django.urls import include,path
from rest_framework.routers import DefaultRouter
from . import views
from .views import PlaylistListCreateAPIView, DownloadSongView

router=DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('playlists/', PlaylistListCreateAPIView.as_view(), name='playlist'),
    path('songs/', views.SongView.as_view(), name='songs'),
    path('song/download/<uuid:pk>/', DownloadSongView.as_view(), name='download_song'),
]