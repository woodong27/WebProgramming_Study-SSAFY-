from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method=='POST':
        #데이터를 제출 했다면 로그인 과정 진행
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    
    else:
        #데이터를 제출한게 아니면 데이터를 받는 과정 진행(로그인 form 제공)
        #django에서 제공하는 login form 사용
        form=AuthenticationForm()
    
    context={
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')