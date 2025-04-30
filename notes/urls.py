from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('notes/<str:id>/add/', views.addView, name='add'),
    path("notes/<str:id>/", views.notes, name="notes"),
    #path("notes/", views.notes, name="notes"),
]