from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('expense/', views.ExpenseListView.as_view(), name='expenses'),
    path('myTrips/', views.TripListView.as_view(), name='myTrips'),       
    path('myTrips/<int:pk>/', views.TripDetailView.as_view(), name='trip-detail'),
    path('expense/<int:pk>/', views.ExpenseDetailView.as_view(), name='expense-detail'),    
    
]
