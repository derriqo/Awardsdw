from django.shortcuts import render,redirect
from .models import Project,Profile,Rating
from django.contrib.auth.decorators import login_required
from .forms import CreateProject
from django.http import Http404

def index(request):
    projects = Project.objects.all()

    return render(request,'index.html',{'projects':projects})

@login_required(login_url='accounts/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user__pk=current_user.id)
    return render(request,'profile.html',{'current_user':current_user,'projects':projects})

@login_required(login_url='accounts/')
def new_project(request):

    if request.method=='POST':
        form = CreateProject(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save( )
            return redirect('home')
    else:
        form = CreateProject()

    return render(request,'addproject.html',{'form':form})

@login_required(login_url='accounts/')
def search_project(request):

    if 'Saka' in request.GET and request.GET["Saka"]:
        idea = request.GET.get("Saka")
        searched_projects = Project.search_by_projectname(idea)
        message = f"{idea}"

        return render(request,'search.html',{'message':message,'projects':searched_projects})

    else:
        message ="You have not searched for any project"
        return render(request,'search.html',{'message':message,})

@login_required(login_url='accounts/')
def rating(request,project_id):    
    projects = Project.objects.get(id=project_id)    
    return render(request,'ratings.html', locals())    




