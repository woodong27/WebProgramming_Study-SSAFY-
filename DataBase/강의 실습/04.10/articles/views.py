from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    commentForm=CommentForm()
    comments=article.comment_set.all()
    context = {
        'article': article,
        'commentForm': commentForm,
        'comments':comments,
        }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user=request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user==article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user==article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', pk=article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    
    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)

def comments_create(request, pk):
    article=Article.objects.get(pk=pk)
    commentForm=CommentForm(request.POST)
    if commentForm.is_valid():
        #save의 commit옵션을 사용해서 DB에 comment를 저장하기 전에 article객체를 저장
        comment=commentForm.save(commit=False)
        comment.article=article
        comment.save()
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)