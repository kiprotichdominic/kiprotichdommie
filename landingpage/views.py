from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView


class LandingPageView(TemplateView):
    template_name = 'landingpage/index.html'