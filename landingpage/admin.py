from django.contrib import admin

# Register your models here.
from .models import PortfolioProject, Testimonial


admin.site.register(PortfolioProject)
admin.site.register(Testimonial)
