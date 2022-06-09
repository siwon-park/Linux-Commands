from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import *
from .serializers.skill import *

User = get_user_model()

# 로드맵 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def roadmap(request):
    roadmap = Skill.objects.all()
    serializer = RoadamapSerializer(roadmap, many=True)
    return Response(serializer.data)

# 로드맵 상세 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def roadmap_detail(request, skill_pk):
    roadmap = get_object_or_404(Skill, pk=skill_pk)
    serializer = RoadamapSerializer(roadmap)
    return Response(serializer.data)

# 로드맵 선택(등록)
@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def roadmap_pick(request, skill_pk, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    roadmap_skill = get_object_or_404(Skill, pk=skill_pk)
    skill = roadmap_skill.id

    if user.user_knowledge.filter(knowledge_skill_id=skill_pk).exists():
        user.user_knowledge.remove(knowledge_skill_id=skill_pk)
        # Knowledge.objects.get(knowledge_skill_id=skill_pk).delete()
    else:
        print('88888888888888')
        # user.user_knowledge.add(skill)
        user.user_knowledge.create(knowledge_skill_id=skill)
    
    serializer = RoadmapPickSerializer(user)
    return Response(serializer.data)
    