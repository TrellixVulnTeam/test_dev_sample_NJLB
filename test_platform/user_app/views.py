from django.contrib.auth import decorators
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
#from test_dev_sample.test_platform import project_app


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
                response = HttpResponseRedirect("/manage/project_manage/")
                #response.set_cookie('user1',username,3600)
                return response
             
            else:
                return render(request, "index.html", {"error": "用户名或者密码错误"})




def logout(request):#清除用户登录状态
    auth.logout(request)
    response =HttpResponseRedirect('/')
    return response


    
