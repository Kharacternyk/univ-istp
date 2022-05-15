from django.contrib import admin
from django.urls import path
from bgclub.views import (
    IndexView,
    NewSessionPlayersView,
    NewSessionTimeView,
    language_chart_view,
    authors_chart_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view()),
    path("session/new/players", NewSessionPlayersView.as_view()),
    path("session/new/time", NewSessionTimeView.as_view()),
    path("chart/game/language", language_chart_view),
    path("chart/game/authors", authors_chart_view),
]
