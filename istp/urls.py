from django.contrib import admin
from django.urls import path
from bgclub.views import IndexView, NewSessionPlayersView, NewSessionTimeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view()),
    path("session/new/players", NewSessionPlayersView.as_view()),
    path("session/new/time", NewSessionTimeView.as_view()),
]
