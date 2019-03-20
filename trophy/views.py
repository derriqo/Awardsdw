from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required


def index(request):
    projects = Project.objects.all()

    return render(request,'index.html',{'projects':projects})

@login_required(login_url='accounts/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user__pk=current_user.id)
    return render(request,'profile.html',{'current_user':current_user,'projects':projects})
