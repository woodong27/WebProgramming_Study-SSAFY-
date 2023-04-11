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
        'commentForm':commentForm,
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
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {'form': form, 'article': article}
    return render(request, 'articles/update.html', context)

def comments_create(request, pk):
    if request.user.is_authenticated:
        article=Article.objects.get(pk=pk)
        commentForm=CommentForm(request.POST)
        if commentForm.is_valid():
            comment=commentForm.save(commit=False)
            comment.article=article
            comment.user=request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')

def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:     
        comment=Comment.objects.get(pk=comment_pk)
        if comment.user==request.user:
            comment.delete()
        return redirect('articles:detail', article_pk)
    return redirect('accounts:login')

def likes(request, article_pk):
    if request.user.is_authenticated:
        article=Article.objects.get(pk=article_pk)
        # Like가 되어있으면 취소
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        # Like가 되어있지 않으면 표시해줌
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')