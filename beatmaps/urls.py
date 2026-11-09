from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path("", views.home, name="home"),

    # Upload page
    path("upload/", views.upload, name="upload"),

    # Download page
    path("download/", views.download, name="download"),

    # Download the actual game
    path("download/game/", views.download_game, name="download_game"),
]

