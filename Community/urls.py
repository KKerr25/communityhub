from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_Events, name="index"),
    path("/<int:pk>/", views.event_Details, name="event-detail"),
    path("event-form/", views.EventFormView.as_view(), name="event-form" )
]
