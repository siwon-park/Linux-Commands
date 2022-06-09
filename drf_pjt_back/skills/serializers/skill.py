from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.serializers.account import SkillSerializer
from skills.models import Knowledge, Skill

User = get_user_model()

# 로드맵 조회 및 상세 조회
class RoadamapSerializer(serializers.ModelSerializer):

    super_skills = SkillSerializer(many=True)

    class Meta:
        model = Skill
        fields = '__all__'


# 로드맵 선택
class RoadmapPickSerializer(serializers.ModelSerializer):
    
    class UserSkillSerializer(serializers.ModelSerializer):
        
        knowledge_skill = SkillSerializer(read_only=True)
        
        class Meta:
            model = Knowledge
            fields = ('id', 'knowledge_skill',)
            
    user_knowledge = UserSkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'user_knowledge', )