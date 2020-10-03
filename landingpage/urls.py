from django.urls import path

# from .views import LandingPageView
from . import views

urlpatterns = [
    path('', views.LandingPage, name='home'),
]
