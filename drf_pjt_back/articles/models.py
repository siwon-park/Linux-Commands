from django.db import models
from django.conf import settings

class Articles(models.Model):
    # 카테고리 항목
    category_choices = [
        ("QnA", "Q&A"),
        ("Info", "정보"),
        ("Talk", "잡담"),
        ("Notice","공지사항"),
    ]
    # 카테고리 필드
    catergory = models.CharField(
        choices=category_choices,
        default="Info",
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 게시글을 작성한 사용자 참조(역참조: "write_article")
    write_article_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='write_article')

    # 게시글을 좋아요한 사용자들(역참조: "like_articles")
    like_article_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")


class Comments(models.Model):
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 댓글 작성자(역참조: "write_comment")
    write_comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="write_comment")

    # 상위 댓글
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child_comment', null=True, blank=True)

    # 댓글을 좋아요한 사용자들(역참조: "like_comments")
    like_comment_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like_comments')
