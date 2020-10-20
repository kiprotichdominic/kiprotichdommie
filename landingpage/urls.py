from django.urls import path

# from .views import ContactPage
from . import views

urlpatterns = [
    path('', views.LandingPage, name='home'),
    # path('', views.contactView, name='contact'),
]
