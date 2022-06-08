from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count
from .models import Article, Comment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny 
from .serializers.article import ArticleListSerializer, ArticleSerializer
from .serializers.comment import CommentListSerializer, CommentSerializer


# 게시글 전체 조회 및 게시글 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list_or_create(request):
    # 게시글 전체 조회
    def article_list():
        articles = Article.objects.annotate(
            commented_article=Count('article_comment', distinct=True),
            like_count=Count('like_article_users', distinct=True)
        ).order_by('-pk')
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)

    # 단일 게시글 생성
    def article_create():
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(write_article_user = request.user)
            return Response(serializer.data)

    if request.method == 'GET':
        return article_list()
    elif request.method == 'POST':
        return article_create()

# 단일 게시글 조회/수정/삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_detail_or_update_or_delete(request, article_pk):
    
    article = get_object_or_404(Article, pk=article_pk)

    # 게시글 상세
    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 게시글 수정
    def article_update():
        if request.user == article.write_article_user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    # 게시글 삭제
    def article_delete():
        if request.user == article.write_article_user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        return article_update()
    elif request.method == 'DELETE':
        return article_delete()

# 게시글 좋아요 등록/해제
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user

    if article.like_article_users.filter(pk=user.pk).exists(): # 이미 좋아요를 등록했다면 해제
        article.like_article_users.remove(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else: # 좋아요를 하지 않았다면 등록
        article.like_article_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

# 전체 댓글 조회 및 댓글 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_list_or_create(request, article_pk):
    
    article = get_object_or_404(Article, pk=article_pk)

    # 전체 댓글 조회(임시)
    def comment_list():
        serializers = CommentListSerializer(article)
        return Response(serializers.data) 

    # 최상위 댓글 생성 
    def root_comment_create():
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(commented_article=article, write_comment_user=request.user)
            serializers = CommentListSerializer(article)
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        return comment_list()
    elif request.method == 'POST':
        return root_comment_create()


# 단일 (대)댓글 수정/삭제    
@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_create_or_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    # 대댓글 생성
    def comment_create():
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(commented_article=article, parent_comment=comment, write_comment_user=request.user)
            serializers = CommentListSerializer(article)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
    
    # 댓글 수정
    def comment_update():
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            serializers = CommentListSerializer(article)
            return Response(serializers.data)

    # 댓글 삭제
    def comment_delete():
        deleted_data = {'content': '삭제된 댓글입니다.'}
        serializer = CommentSerializer(instance=comment, data=deleted_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            serializers = CommentListSerializer(article)
            return Response(serializers.data, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'POST':
        return comment_create()
    elif request.method == 'PUT':
        return comment_update()
    elif request.method == 'DELETE':
        return comment_delete()


# 댓글 좋아요 등록/해제
@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_like(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user

    # 이미 좋아요를 누른 상태라면
    if comment.like_comment_users.filter(pk=user.pk).exists():
        comment.like_comment_users.remove(user)
        serializers = CommentListSerializer(article)
        return Response(serializers.data)
    else: # 좋아요 등록
        comment.like_comment_users.add(user)
        serializers = CommentListSerializer(article)
        return Response(serializers.data)