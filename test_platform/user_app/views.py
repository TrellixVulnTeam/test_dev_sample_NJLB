from django.contrib.auth import decorators
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, response
from django.contrib import auth
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    return render(request, "index.html")


# 处理登录请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")

        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或者密码为空"})

        else:
            user=auth.authenticate(username=username,password=password)
            print(user)
            print(type(user))
            if user is not None:
                auth.login(request,user) #记录用户登录状态
                request.session['user1']=username
                response = HttpResponseRedirect("/project_manage/")
                #response.set_cookie('user1',username,3600)
                return response
             
            else:
                return render(request, "index.html", {"error": "用户名或者密码错误"})


@login_required #判断用户是否登录
def project_manage(request):
    username =request.session.get('user1','')
    #username =request.COOKIES.get('user1','')
    return render(request, "project_manage.html",{'user':username})

def logout(request):
    auth.logout(request)
    response =HttpResponseRedirect('/')
    return response


    
