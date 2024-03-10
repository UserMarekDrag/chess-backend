from django.urls import path
from .views import GameListCreateAPIView, GameDetailAPIView

urlpatterns = [
    path('games/', GameListCreateAPIView.as_view(), name='game-list-create'),
    path('games/<int:pk>/', GameDetailAPIView.as_view(), name='game-detail'),
]
