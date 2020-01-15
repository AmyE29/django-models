from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Flavor

# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Flavor
    context_object_name = 'all_flavors'

class FlavorDetailView(DetailView):
    template_name = 'flavors_details.html'
    model = Flavor