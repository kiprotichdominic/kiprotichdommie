from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
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


# class ContactPage(TemplateView):
#     template_name = "landingpage/contact.html"

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "landingpage/contact.html", {'form': form})