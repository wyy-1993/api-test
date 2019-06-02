from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth

def login(request):
    return render(request, './t_login/login.html')

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            request.session['user'] = username
            response = HttpResponseRedirect('/debug/')
            return response
        else:
            return render(request,'./t_login/login.html',{'error':'username or password error!'})
