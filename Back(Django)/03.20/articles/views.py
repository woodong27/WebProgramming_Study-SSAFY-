from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles=Article.objects.all()
    context={
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article=Article.objects.get(pk=pk)
    context={
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        
        #DB에 입력받은 article 저장
        article=Article(title=title, content=content)
        
        #Data가 유효한지 검사하는 코드가 올 공간
        
        article.save()
        
        #저장 후 새로운 페이지로 이동 : redirect
        return redirect('articles:index')
    
    else:
        return render(request,'articles/create.html')

def update(request, pk):
    article=Article.objects.get(pk=pk)
    if request.method=='POST':
        article.title=request.POST.get('title')
        article.content=request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context={
            'article':article,
        }
        return render(request,'articles/update.html', context)
    
def delete(request, pk):
    article=Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# def edit(request, pk):
#     article=Article.objects.get(pk=pk)
#     context={
#         'article':article,
#     }
#     return render(request, 'articles/edit.html', context)

# def update(request, pk):
#     article=Article.objects.get(pk=pk)
#     article.title=request.POST.get('title')
#     article.content=request.POST.get('content')
#     article.save()
#     return redirect('articles:detail', article.pk)