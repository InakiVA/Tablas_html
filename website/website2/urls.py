from django.urls import path
from .views import JUgadorChartView

urlpatterns = [
    path('', JUgadorChartView.as_view(), name="home")
]