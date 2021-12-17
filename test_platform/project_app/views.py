from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import  Project
# Create your views here.


@login_required #判断用户是否登录
def project_manage(request):
    username =request.session.get('user1','')
    #username =request.COOKIES.get('user1','')
    project_all = Project.objects.all()
    return render(request, "project_manage.html",{
        'user':username,
        'projects':project_all,
        "type":"list"
    })


@login_required 
def add_project(request):
    
    return render(request, "project_manage.html",{"type":"add"})