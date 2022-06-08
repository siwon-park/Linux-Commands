from articles.models import Article, Comment
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .comment import CommentListSerializer
User = get_user_model()

# 전체 게시글 조회 및 단일 게시글 생성
class ArticleListSerializer(serializers.ModelSerializer):

    # 유저 정보를 입력받기 위한 시리얼라이저
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('id', 'username',)
    # 게시글 작성자
    write_article_user = UserSerializer(read_only=True)
    # 게시글의 댓글 수
    comment_count = serializers.IntegerField(source='article_comment.count', read_only=True)
    # 게시글의 좋아요 수
    like_count = serializers.IntegerField(source='like_article_users.count', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'catergory', 'title', 'content', 'created_at', 'updated_at', 'write_article_user', 'comment_count', 'like_count',)


# 단일 게시글 조회/수정/삭제
class ArticleSerializer(serializers.ModelSerializer):
    # 유저 정보를 입력받기 위한 시리얼라이저
    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = User
            fields = ('id', 'username',)
    # 게시글 작성자
    write_article_user = UserSerializer(read_only=True)
    # 게시글의 댓글 수
    comment_count = serializers.IntegerField(source='article_comment.count', read_only=True)
    # 게시글의 좋아요 수
    like_count = serializers.IntegerField(source='like_article_users.count', read_only=True)

    article_comment = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'catergory', 'title', 'content', 'created_at', 'updated_at', 'write_article_user', 'comment_count', 'like_count', 'article_comment',)
