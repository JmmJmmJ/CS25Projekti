from django.urls import path

from . import views

#path("details/<int:id1>/", views.details, name="details"),
urlpatterns = [
    path("", views.index, name="index"),
    path("details/<str:id1>/", views.details, name="details"),
    path('add/', views.addView, name='add'),
]