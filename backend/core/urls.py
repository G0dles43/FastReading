from django.urls import path
from . import views
from .views import api_status


urlpatterns = [
    path("", views.index, name="index"),
    path('status/', api_status),
]