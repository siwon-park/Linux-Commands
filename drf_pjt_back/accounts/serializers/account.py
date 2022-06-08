from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model
from skills.models import Knowledge, Skill

User = get_user_model()

class AccountSerializer(serializers.ModelSerializer):
    
    profile_img = serializers.CharField(max_length=300)
    school = serializers.CharField(max_length=30) # 학력 및 학교
    career = serializers.CharField(max_length=200) # 커리어 경험
    introduce = serializers.CharField(max_length=200) # 자기 소개
    github_url = serializers.CharField(max_length=200)
    blog_url = serializers.CharField(max_length=200)
    notion_url = serializers.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('profile_img', 'school', 'career', 'introduce', 'github_url', 'blog_url', 'notion_url',)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_img'] = self.validated_data.get('profile_img', '')
        data['school'] = self.validated_data.get('school', '')
        data['career'] = self.validated_data.get('career', '')
        data['introduce'] = self.validated_data.get('introduce', '')
        data['github_url'] = self.validated_data.get('github_url', '')
        data['blog_url'] = self.validated_data.get('blog_url', '')
        data['notion_url'] = self.validated_data.get('notion_url', '')

        return data


class SkillSerializer(serializers.ModelSerializer):
        class Meta:
            model = Skill
            fields = '__all__'


class UserSeializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields = '__all__'


# 프로필 조회, 수정, 사용자 로드맵 조회, 개발 동료 조회
class ProfileSerializer(serializers.ModelSerializer):
    
    class UserSkillSerializer(serializers.ModelSerializer):
        
        knowledge_skill = SkillSerializer(read_only=True)
        
        class Meta:
            model = Knowledge
            fields = '__all__'
            
    user_knowledge = UserSkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile_img', 'school', 'career', 'introduce', 'github_url', 'blog_url', 'notion_url', 'bookmarking', 'user_knowledge', )


# 회원 탈퇴

# 사용자 로드맵 수정, 로드맵 선택
class ProfileRoadmapSerializer(serializers.ModelSerializer):
    
    class UserSkillSerializer(serializers.ModelSerializer):
        
        knowledge_skill = SkillSerializer(read_only=True)
        
        class Meta:
            model = Knowledge
            fields = '__all__'
            
    user_knowledge = UserSkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'user_knowledge', )


# 사용자 로드맵 상세 조회
class UserRoadmapDetailSerializer(serializers.ModelSerializer):

    class KnowledgeSkillSerializer(serializers.ModelSerializer):
        
        class NeedSkillSerializer(serializers.ModelSerializer):
            
            class Meta:
                model = Skill
                fields = ('id', 'need_skills',)
        
        class Meta:
            model = Knowledge
            fields = '__all__'
    
    user_knowledge = KnowledgeSkillSerializer(many=True, read_only=True)


    class Meta:
        model = User
        fields = '__all__'

# 북마크 조회, 등록 및 해제
class BookmarkSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'bookmarking',)




