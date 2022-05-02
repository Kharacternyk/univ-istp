from django_tables2 import Table
from bgclub.models import GameLocalization


class GameLocalizationTable(Table):
    class Meta:
        model = GameLocalization
        attrs = {
            "class": "table table-striped table-hover table-bordered",
            "th": {"class": "table-dark"},
        }
