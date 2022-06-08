from articles.models import Article, Comment
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# 부모 댓글 조회
class ParentCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('parent_comment',)

# 댓글 생성 및 수정
class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = User
            fields = ('id', 'username',)
        
    # 댓글의 작성자
    write_comment_user = UserSerializer(read_only=True)
    # 부모 댓글
    parent_comment = ParentCommentSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'write_comment_user', 'commented_article', 'parent_comment',)
        read_only_fields = ('commented_article',)

# 상위 부모 댓글 조회용 중간 시리얼라이저
class ParentCommentListSerializer(serializers.ModelSerializer):
    
    parent_comments_list = serializers.SerializerMethodField()
    
    like_count = serializers.IntegerField(source='like_comment_users.count', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at', 'parent_comment', 'parent_comments_list', 'commented_article', 'write_comment_user', 'like_count')
        read_only_fields = ('write_comment_user', )

    def get_parent_comments_list(self, instance):
        serializer = self.__class__(instance.parent_comments_list, many=True)
        serializer.bind('', self)
        return serializer.data

# 전체 댓글 조회
class CommentListSerializer(serializers.ModelSerializer):
    
    reply_comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = ('id', 'reply_comments',)

    def get_reply_comments(self, obj):
        reply_comments = obj.article_comment.filter(parent_comment=True)
        serializer = ParentCommentListSerializer(reply_comments, many=True)
        return serializer.data
