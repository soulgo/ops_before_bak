from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def LoginShowView(request,*args,**kwargs):
    return render(request, 'login.html')

def LoginView(request,*args,**kwargs):
    '''
        登录逻辑
    '''
    username = request.GET.get('username')
    password = request.GET.get('password')
    if username and password:
        userinfo = ('51reboot', '123456')
        if username == userinfo[0] and password == userinfo[1]:
            login_result = 'login succ'
        else:
            login_result = 'login fail'
    else:
        login_result = 'username and password is required'
    return HttpResponse(login_result)

def LoginAuthView(request,*args,**kwargs):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            userinfo = ('51reboot','123456')
            if username == userinfo[0] and password == userinfo[1]:
                login_result = 'login succ'
            else:
                login_result = 'login fail'
                # return redirect('/api/login_auth/')  #重定向到某个页面
                return render(request,'login.html',context={'msg' : 'login fail'})
        else:
            login_result = 'username and password is requried'
        return HttpResponse(login_result)