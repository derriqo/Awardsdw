from django.shortcuts import render
from django.views.generic import ListView
from .models import Project


# Create your views here.
class HomePageView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'all_projects_list'