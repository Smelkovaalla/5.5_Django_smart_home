from django.urls import path

from measurement.views import SensorsView, TemperatureView

urlpatterns = [
    path('temperature/', TemperatureView.as_view()),
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorsView.as_view()),
]