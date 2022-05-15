from django.forms import ModelForm, ValidationError, CheckboxSelectMultiple
from bgclub.models import PlaySession, GameLocalization, ClubMember


class PlaySessionForm(ModelForm):
    def clean(self):
        start_time = self.cleaned_data.get("start_time")
        end_time = self.cleaned_data.get("end_time")
        if start_time and end_time and end_time < start_time:
            raise ValidationError(
                {"end_time": "Сеанс не може закінчитись раніше за час початку."}
            )


class PrefilledPlaySessionForm(PlaySessionForm):
    class Meta:
        model = PlaySession
        fields = "__all__"
        widgets = {
            "game_localizations": CheckboxSelectMultiple,
            "club_members": CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        game_localizations = kwargs.pop("game_localizations")
        club_members = kwargs.pop("club_members")
        super().__init__(*args, **kwargs)
        self.initial["game_localizations"] = game_localizations
        self.initial["club_members"] = club_members


class ClubMemberForm(ModelForm):
    def clean(self):
        phone = self.cleaned_data.get("phone")
        if phone and phone < 1e6:
            raise ValidationError({"phone": "Телефон має містити не менше шести цифр."})


class GameLocalizationForm(ModelForm):
    MIN_CATALOG_YEAR = 2015

    def clean(self):
        barcode = self.cleaned_data.get("barcode")
        publishing_date = self.cleaned_data.get("publishing_date")
        in_catalog_since_date = self.cleaned_data.get("in_catalog_since_date")

        if barcode:
            digits = int(log10(barcode))
            if not 12 <= digits <= 13:
                raise ValidationError(
                    {
                        "barcode": f"Штрих-код має мати 12 або 13 цифр, отримано {digits}."
                    }
                )

        if (
            publishing_date
            and in_catalog_since_date
            and in_catalog_since_date < publishing_date
        ):
            raise ValidationError(
                {
                    "in_catalog_since_date": "Гра не може з'явитись у каталозі до видання."
                }
            )

        if in_catalog_since_date and in_catalog_since_date.year < self.MIN_CATALOG_YEAR:
            raise ValidationError(
                {
                    "in_catalog_since_date": "Гра не може з'явитись у каталозі "
                    + f"раніше {self.MIN_CATALOG_YEAR} року, коли відчинився клуб."
                }
            )


class GameForm(ModelForm):
    def clean(self):
        min_players = self.cleaned_data.get("min_players")
        max_players = self.cleaned_data.get("max_players")
        if min_players == 0:
            raise ValidationError({"min_players": "Гра не може проходити без гравців."})
        if max_players == 0:
            raise ValidationError({"max_players": "Гра не може проходити без гравців."})
        if min_players and max_players and min_players > max_players:
            raise ValidationError(
                {
                    "max_players": "Максимальна кількість гравців не може бути меншою за мінімальну."
                }
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
