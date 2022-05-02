from django_tables2 import SingleTableView

from bgclub.models import GameLocalization
from bgclub.tables import GameLocalizationTable


class IndexView(SingleTableView):
    template_name = "index.html"
    model = GameLocalization
    table_class = GameLocalizationTable
