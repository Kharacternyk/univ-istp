from django.views.generic import ListView
from bgclub.models import GameLocalization


class IndexView(ListView):
    template_name = "index.html"
    model = GameLocalization
