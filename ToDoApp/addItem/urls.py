from django.urls import path
from . import views


urlpatterns = [
    path("", views.addItem, name="index"),
    path("success/<task>/", views.successfulAddition, name="successfulAddition")
]