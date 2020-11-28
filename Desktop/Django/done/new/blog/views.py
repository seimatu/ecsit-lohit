from django.shortcuts import render,redirect
from .models import Project
# Create your views here.

def project_index(request):
    projects=Project.objects.all()

    return render(request,'projects/projects_index.html', {
        'projects':projects
        })


#models function
def project_detail(request,pk):
    project=Project.objects.get(pk=pk)
   
    return render(request,'projects/project_detail.html', {
        'project':project
    })