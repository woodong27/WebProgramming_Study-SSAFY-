from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentSerializer, ArticleDetailSerializer
from drf_yasg.utils import swagger_auto_schema



# Create your views here.
@swagger_auto_schema(methods=['POST'], request_body=ArticleListSerializer)
@api_view(['GET', 'POST'])
def article_list(request):
    # 목록을 출력하는 요청일 때(method='GET'일 때)
    if request.method=='GET':
        articles=get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    # 새로운 데이터를 추가할 때(method='POST'일 떄)
    elif request.method=='POST':
        serializer=ArticleListSerializer(data=request.data)
        # raise_exception=True를 추가하면 유효성 검사를 통과하지 못했을 때 drf에서 내부적으로 오류 코드를 실행해 줌
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 데이터가 유효하면 직렬화해서 전송
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 데이터 생성이 실패했을 때는 bad request를 응답
        # Response내부에는 빈 객체를 줘도 괜찮음
        # 에러가 났을 때 그걸 표시해줄 수도 있고, 그냥 빈창이 나오게 할 수도 있음
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=['PUT'], request_body=ArticleListSerializer)
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article=get_object_or_404(Article, pk=article_pk)
    if request.method=='GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    # request.method='DELETE'로 삭제 요청일 때
    elif request.method=='DELETE':
        article.delete()
        # 빈 객체 대신 해당 게시글이 삭제 되어서 비어있다는 표시를 띄워줌
        return Response(status=status.HTTP_204_NO_CONTENT)
    # request.method='PUT'으로 수정 요청일 때
    elif request.method=='PUT':
        # 기존 instance에 입력한 데이터를 넣고 직렬화 시켜줌
        serializer=ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

# 전체 댓글 조회
# @api_view(['GET'])
# def comment_list(request):
#     comments=get_list_or_404(Comment)
#     serializer=CommentSerializer(comments, many=True)
#     return Response(serializer.data)

# 댓글 상세 조회, 삭제, 수정
@swagger_auto_schema(methods=['PUT'], request_body=CommentSerializer())
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

# 댓글 생성+해당 게시글의 모든 댓글 조회
@swagger_auto_schema(methods=['POST'], request_body=CommentSerializer)
@api_view(['GET','POST'])
def comment_list(request, article_pk):
    article=get_object_or_404(Article, pk=article_pk)
    if request.method=='GET':
        comments=article.comments.all()
        serializer=CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # save에 옵션을 추가해서 serialize되는 과정에서 article 객체에 추가적인 데이터를 넘겨서 저장
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)