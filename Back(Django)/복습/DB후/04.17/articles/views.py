from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleDetailSerializer, CommentSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
# article 전체 조회, article 생성
@swagger_auto_schema(methods=['POST'], request_body=ArticleListSerializer)
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method=='GET':
        articles=get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# article 상세 조회, 삭제, 수정
@swagger_auto_schema(methods=['PUT'], request_body=ArticleDetailSerializer)
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article=get_object_or_404(Article, pk=article_pk)
    if request.method=='GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    elif request.method=='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method=='PUT':
        serializer=ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 댓글 생성, 해당 게시글의 모든 댓글 조회
@swagger_auto_schema(methods=['POST'], request_body=CommentSerializer)
@api_view(['GET', 'POST'])
def comment_list(request, article_pk):
    article=get_object_or_404(Article, pk=article_pk)
    if request.method=='GET':
        comments=article.comment_set.all()
        serializer=CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# 댓글 상세 조회, 삭제, 수정
@swagger_auto_schema(methods=['PUT'], request_body=CommentSerializer)
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment=get_object_or_404(Comment, pk=comment_pk)
    if request.method=='GET':
        serializer=CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method=='DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='PUT':
        serializer=CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)