from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('expense/', views.ExpenseListView.as_view(), name='expenses'),
    path('myTrips/', views.TripListView.as_view(), name='myTrips'),
]
