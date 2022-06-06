from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_img = models.CharField(max_length=300, null=True, blank=True)
    school = models.CharField(max_length=30, null=True, blank=True) # 학력 및 학교
    career = models.TextField(null=True, blank=True) # 커리어 경험
    introduce = models.TextField(null=True, blank=True) # 자기 소개
    github_url = models.CharField(max_length=200, null=True, blank=True)
    blog_url = models.CharField(max_length=200, null=True, blank=True)
    notion_url = models.CharField(max_length=200, null=True, blank=True)
    # 북마킹
    bookmarking = models.ManyToManyField('self', symmetrical=False, related_name='bookmarked_users', blank=True)