from django.shortcuts import render, redirect
from .models import Article
from  .forms import ArticleForm

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
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            article=form.save()
            return redirect('articles:detail', article.pk)
        
    else: 
        form=ArticleForm()
    
    context={
        'form':form,
    }
    #작성한 글이 유효하지 않으면 다시 create로 이동
    return render(request, 'articles/create.html', context)
    
def update(request, pk):
    article=Article.objects.get(pk=pk)
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        #article의 data가 form에 채워짐
        form=ArticleForm(instance=article)
        
    context={
        'form':form,
        'article':article,
    }
    return render(request, 'articles/update.html', context)
    
def delete(request, pk):
    article=Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')