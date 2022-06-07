from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.serializers.account2 import SkillSerializer
from skills.models import Knowledge, Skill

# 로드맵 조회 및 상세 조회
class Roadamap(serializers.ModelSerializer):

    knowledge_skill = SkillSerializer(read_only=True)

    class Meta:
        model = Knowledge
        fields = '__all__'


# need_skills 입력 serializers
class NeedInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('name', 'need_skills', )