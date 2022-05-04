from django_tables2 import SingleTableView

from django.views.generic.edit import CreateView

from bgclub.models import GameLocalization, ClubMember, PlaySession
from bgclub.tables import GameLocalizationTable, ClubMemberTable
from bgclub.forms import PrefilledPlaySessionForm


class IndexView(SingleTableView):
    template_name = "index.html"
    model = GameLocalization
    table_class = GameLocalizationTable


class NewSessionPlayersView(SingleTableView):
    template_name = "new_session_players.html"
    model = ClubMember
    table_class = ClubMemberTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["barcodes"] = self.request.GET.getlist("barcode")
        return context


class NewSessionTimeView(CreateView):
    template_name = "new_session_time.html"
    model = PlaySession
    form_class = PrefilledPlaySessionForm
    success_url = "/"

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs["game_localizations"] = self.request.GET.getlist("barcode")
        kwargs["club_members"] = self.request.GET.getlist("player_id")
        return kwargs
