from django.urls import path
from .views import *

app_name = 'comp'

urlpatterns = [
    path('accessories/', AccessoriesListView.as_view(), name='accessories'),
    path('accessories/<int:pk>/', AccessoriesDetailView.as_view(), name='accessories-detail'),
    path('phones/<int:pk>/', ComputerDetailView.as_view(), name='computers-detail'),
    path('', ComputerListView.as_view(), name='computer'),
]
