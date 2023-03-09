from django.urls import path
from .views import *

app_name = 'phones'

urlpatterns = [
    path('accessories/', AccessoriesListView.as_view(), name='accessories'),
    path('phones/', PhoneListView.as_view(), name='phone'),
    path('accessories/<int:pk>/', AccessoriesDetailView.as_view(), name='accessories-detail'),
    path('phones/<int:pk>/', PhoneDetailView.as_view(), name='phone-detail'),
]
