from django.db import models
from django.conf import settings

class Type(models.Model):
    name = models.CharField(max_length=50) # language, framework, etc..


class Skill(models.Model):
    name = models.CharField(max_length=50) 
    category = models.CharField(max_length=50) # python, djanog, etc...
    difficulty = models.CharField(max_length=20) # basic, advanced, etc ...
    logo_img = models.CharField(max_length=200, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True) # 학습 난이도
    skill_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type_skill')

    # 선행/후행 재귀 관계
    need_skills = models.ManyToManyField('self', symmetrical=False, related_name='super_skills', blank=True)

    # User와의 중개 테이블 작성
    skill_list = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Knowledge')

class Knowledge(models.Model):
    knowledge_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_knowledge')
    knowledge_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill_knowledge')
    knowledge_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type_knowledge')
    level = models.IntegerField(null=True, blank=True) # 익힌 정도
    checked = models.BooleanField() # 확인 
