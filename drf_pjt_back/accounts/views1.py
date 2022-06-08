from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import *
from .serializers.account import *

User = get_user_model()


# 프로필 조회 및 수정
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    def profile_get():
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    def profile_put():
        if request.user == user:
            serializer = ProfileSerializer(instance=user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = ProfileSerializer(user)
                return Response(serializer.data)
    
    if request.method == 'GET':
        return profile_get()
    elif request.method == 'PUT':
        return profile_put()

# 회원 탈퇴

# 사용자 로드맵 조회, 수정
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_roadmap(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    def roadmap_get():
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    def roadmap_put():
        if request.user == user:
            serializer = ProfileRoadmapSerializer(instance=user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer = ProfileRoadmapSerializer(user)
                return Response(serializer.data)

    if request.method == 'GET':
        return roadmap_get()
    elif request.method == 'PUT':
        return roadmap_put()

# 사용자 로드맵 상세 조회(이행 수준)
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_roadmap_detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)
    

# 북마크 조회, 등록 및 해제
@api_view(['GET' ,'POST'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def bookmark(request, user_pk):

    def bookmark_get():
        # 나의 북마크 조회
        user = get_object_or_404(User, pk=user_pk)
        serializer = BookmarkSerializers(user)
        return Response(serializer.data)

    def bookmark_post():
        # user_pk : 북마크를 하려는 사용자의 pk
        bookmarked_user = get_object_or_404(User, pk=user_pk)
        user = request.user
        # 본인 확인
        if bookmarked_user != user:
            if user.bookmarking.filter(pk=bookmarked_user.pk).exists():
                user.bookmarking.remove(bookmarked_user)
            else:
                user.bookmarking.add(bookmarked_user)

            serializer = BookmarkSerializers(user)
            return Response(serializer.data)
    
    if request.method == 'GET':
        return bookmark_get()
    elif request.method == 'POST':
        return bookmark_post()
        
# 개발 동료 찾기
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def partners(request):
    users = User.objects.order_by('?')
    serializers = ProfileSerializer(users, many=True)
    return Response(serializers.data)
