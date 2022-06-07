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
    # 댓글의 좋아요 수
    like_count = serializers.IntegerField(source='like_comment_users.count', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'write_comment_user', 'commented_article', 'parent_comment', 'like_count',)




# 전체 댓글 조회
class CommentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id',)