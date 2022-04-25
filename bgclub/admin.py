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
            raise ValidationError(
                {"end_time": "Сеанс не може закінчитись раніше за час початку."}
            )


class ClubMemberForm(ModelForm):
    def clean(self):
        phone = self.cleaned_data.get("phone")
        if phone and phone < 1e6:
            raise ValidationError({"phone": "Телефон має містити не менше шести цифр."})


class GameLocalizationForm(ModelForm):
    def clean(self):
        barcode = self.cleaned_data.get("barcode")
        if not barcode:
            return
        digits = int(log10(barcode))
        if not 12 <= digits <= 13:
            raise ValidationError(
                {"barcode": f"Штрих-код має мати 12 або 13 цифр, отримано {digits}."}
            )


class AuthorshipForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["author"].label = "автор"
        self.fields["game"].label = "гра"


class PlayerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["play_session"].label = "сеанс"
        self.fields["club_member"].label = "гравець"


class ItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["play_session"].label = "сеанс"
        self.fields["game"].label = "гра"


class InlineAuthorship(admin.TabularInline):
    form = AuthorshipForm
    model = models.Authorship
    extra = 1


class InlinePlayer(admin.TabularInline):
    form = PlayerForm
    model = models.Player
    extra = 2


class InlineItem(admin.TabularInline):
    form = ItemForm
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


@admin.register(models.Author, models.Game)
class AuthorshipAdmin(NarrowTextAdmin):
    inlines = tuple([InlineAuthorship])


@admin.register(models.PlaySession)
class PlaySessionsAdmin(NarrowTextAdmin):
    form = PlaySessionForm
    inlines = (InlineItem, InlinePlayer)


@admin.register(models.ClubMember)
class ClubMembersAdmin(NarrowTextAdmin):
    form = ClubMemberForm


@admin.register(models.GameLocalization)
class GameLocalizationsAdmin(NarrowTextAdmin):
    form = GameLocalizationForm
