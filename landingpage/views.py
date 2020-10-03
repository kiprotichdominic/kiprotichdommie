from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView

from .models import PortfolioProject, Testimonial


# class LandingPageView(ListView):
#     template_name = 'landingpage/index.html'

#     def get_context_data(self, **kwargs):
#         context = super(LandingPageView, self).get_context_data(**kwargs)
#         context['portfolio_projects'] = PortfolioProject.objects.all()
#         return context


def LandingPage(request):
    p_list = PortfolioProject.objects.all()
    t_list = Testimonial.objects.all()
    context = {
        "projects": p_list,
        "testimonials": t_list,
    }
    return render(request, "landingpage/index.html", context)
