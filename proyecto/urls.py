from django.urls import path
from proyecto.views import inicio


urlpatterns = [
    path('', inicio),
]