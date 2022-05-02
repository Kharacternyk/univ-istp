from django_tables2 import SingleTableView

from bgclub.models import GameLocalization, Game
from bgclub.tables import GameLocalizationTable


class IndexView(SingleTableView):
    template_name = "table.html"
    model = GameLocalization
    table_class = GameLocalizationTable
