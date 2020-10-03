from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView

from .models import PortfolioProject


class LandingPageView(ListView):
    model=PortfolioProject
    template_name='landingpage/index.html'
