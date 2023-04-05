from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

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
    # request.user.delete()
    # 반드시 delete후에 logout을 해줘야 함
    auth_logout(request)
    return redirect('articles:index')

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

def changepw(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            #비밀번호 변경 후 로그인이 풀리는 것을 방지하기 위해 추가
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form=PasswordChangeForm(request.user)
        
    context={
        'form':form,
    }
    return render(request, 'accounts/changepw.html', context)