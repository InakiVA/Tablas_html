from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Jugador

# Create your views here.
class JUgadorChartView(TemplateView):
    template_name = 'website2/main.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["qs"] = Jugador.objects.all()
        return ctx