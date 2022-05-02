from django_tables2 import Table, Column, ManyToManyColumn
from django.utils.html import format_html, format_html_join
from bgclub.models import GameLocalization, Game


class DarkTableMeta:
    attrs = {
        "class": "table table-striped table-hover table-bordered",
        "th": {"class": "table-dark"},
    }


class GameLocalizationTable(Table):
    name = Column(verbose_name="Гра")
    other_localizations = Column(
        verbose_name="Іншомовні варіанти", empty_values=(), orderable=False
    )
    authors = ManyToManyColumn(accessor="game__authors")
    playtime = Column(accessor="game__playtime")
    players = Column(
        verbose_name="Кількість гравців",
        empty_values=(),
        order_by=("game__min_players", "game__max_players"),
    )
    category = Column(accessor="game__category")

    def render_name(self, value, record):
        return format_html(
            '<span title="{}" id="{}">{}</span>', record.barcode, record.barcode, value
        )

    def render_other_localizations(self, record):
        return (
            format_html_join(
                ", ",
                '<a href="#{}">{}</a>',
                (
                    (localization.barcode, localization.name)
                    for localization in GameLocalization.objects.filter(
                        game_id=record.game_id
                    )
                    if localization.barcode != record.barcode
                ),
            )
            or "—"
        )

    def render_players(self, record):
        max = record.game.max_players
        min = record.game.min_players
        if max != min:
            return f"{min}-{max}"
        return f"{min}"

    class Meta(DarkTableMeta):
        model = GameLocalization
        fields = (
            "name",
            "other_localizations",
            "in_catalog_count",
            "publishing_date",
            "in_catalog_since_date",
            "language",
            "publisher",
        )
