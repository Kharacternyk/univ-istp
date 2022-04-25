from django.contrib import admin
from django.forms import Textarea
from django.db.models import TextField
from django.forms import ModelForm, ValidationError
from bgclub import models
from math import log10


class PlaySessionForm(ModelForm):
    def clean(self):
        start_time = self.cleaned_data.get("start_time")
        end_time = self.cleaned_data.get("end_time")
        if start_time and end_time and end_time < start_time:
            raise ValidationError({"end_time": "Must be after the start time."})


class ClubMemberForm(ModelForm):
    def clean(self):
        phone = self.cleaned_data.get("phone")
        if phone and phone < 1e6:
            raise ValidationError({"phone": "Must have at least 6 digits."})


class GameLocalizationForm(ModelForm):
    def clean(self):
        barcode = self.cleaned_data.get("barcode")

        if not barcode:
            return

        if barcode < 0:
            raise ValidationError({"barcode": "Must be a positive integer."})

        digits = int(log10(barcode))
        if not 12 <= digits <= 13:
            raise ValidationError(
                {"barcode": f"Must have either 12 or 13 digits, got {digits}."}
            )


class InlineAuthorship(admin.TabularInline):
    model = models.Authorship
    extra = 1


class InlinePlayers(admin.TabularInline):
    model = models.Players
    extra = 2


class InlineItems(admin.TabularInline):
    model = models.PlaySessionItems
    extra = 1


@admin.register(
    models.Categories,
    models.Countries,
    models.Languages,
    models.Publishers,
)
class NarrowTextAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {"widget": Textarea(attrs={"rows": 1, "cols": 80})},
    }


@admin.register(models.Authors, models.Games)
class AuthorshipAdmin(NarrowTextAdmin):
    inlines = tuple([InlineAuthorship])


@admin.register(models.PlaySessions)
class PlaySessionsAdmin(NarrowTextAdmin):
    form = PlaySessionForm
    inlines = (InlineItems, InlinePlayers)


@admin.register(models.ClubMembers)
class ClubMembersAdmin(NarrowTextAdmin):
    form = ClubMemberForm


@admin.register(models.GameLocalizations)
class GameLocalizationsAdmin(NarrowTextAdmin):
    form = GameLocalizationForm
