from django.contrib import admin
from django.forms import Textarea
from django.db.models import TextField
from bgclub import models
from bgclub import forms
from math import log10


class InlineAuthorship(admin.TabularInline):
    form = forms.AuthorshipForm
    model = models.Authorship
    extra = 1


class InlinePlayer(admin.TabularInline):
    form = forms.PlayerForm
    model = models.Player
    extra = 2


class InlineItem(admin.TabularInline):
    form = forms.ItemForm
    model = models.PlaySessionItem
    extra = 1


@admin.register(
    models.Category,
    models.Country,
    models.Language,
    models.Publisher,
)
class NarrowTextAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {"widget": Textarea(attrs={"rows": 1, "cols": 80})},
    }


@admin.register(models.Author)
class AuthorsAdmin(NarrowTextAdmin):
    inlines = tuple([InlineAuthorship])


@admin.register(models.Game)
class GamesAdmin(NarrowTextAdmin):
    form = forms.GameForm
    inlines = tuple([InlineAuthorship])


@admin.register(models.PlaySession)
class PlaySessionsAdmin(NarrowTextAdmin):
    form = forms.PlaySessionForm
    inlines = (InlineItem, InlinePlayer)


@admin.register(models.ClubMember)
class ClubMembersAdmin(NarrowTextAdmin):
    form = forms.ClubMemberForm


@admin.register(models.GameLocalization)
class GameLocalizationsAdmin(NarrowTextAdmin):
    form = forms.GameLocalizationForm
