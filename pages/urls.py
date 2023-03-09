from django.urls import path
from pages.views import HomeTemplateViews, ContactCreateViews

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreateViews.as_view(), name='contact'),
    path('', HomeTemplateViews.as_view(), name='home'),
]
