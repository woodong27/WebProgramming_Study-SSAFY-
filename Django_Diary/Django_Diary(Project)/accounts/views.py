from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    
    else:
        form=AuthenticationForm()
    
    context={
        'form':form,
    }
    
    return render(request, 'accounts/login.html', context)

@require_safe
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request, user)
            return redirect('articles:index')
    
    else:
        form=CustomUserCreationForm()
        
    context={
        'form':form,
    }
    
    return render(request, 'accounts/signup.html', context)

@require_POST
def delete(request):
    user=request.user
    user.delete()
    auth_logout(request)
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method=='POST':
        form=CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
        
    else:
        form=CustomUserChangeForm(instance=request.user)
    
    context={
        'form':form,
    }
    
    return render(request, 'accounts/update.html', context)

@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            #비밀번호 변경 후 로그인이 풀리는 것을 방지하기 위해 session을 업데이트 해줌
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    
    else:
        form=PasswordChangeForm(request.user)
        
    context={
        'form':form,
    }
    
    return render(request, 'accounts/change_password.html', context)