from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from .models import Article
from django.core import serializers
from .serializers import ArticleSerializer

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles=Article.objects.all()
    articles_json=[]
    
    for article in articles:
        articles_json.append(
            {
                'id':article.pk,
                'title':article.title,
                'content':article.content,
                'created_at':article.created_at,
                'updated_at':article.updated_at,
            }
        )
    
    # JsonResponse를 사용해서 json을 반환
    return JsonResponse(articles_json, safe=False)


def article_json_2(request):
    articles=Article.objects.all()
    # serializer를 사용해서 데이터를 serialize
    data=serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')

#DRF사용시에는 api_view decorator가 필수
@api_view(['GET'])
def article_json_3(request):
    articles=Article.objects.all()
    # serializers.py에서 만든 ArticleSerializer 사용
    serializer=ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_list(request):
    articles=Article.objects.all()
    serializer=ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article=Article.objects.get(pk=article_pk)
    serializer=ArticleSerializer(article)
    return Response(serializer.data)