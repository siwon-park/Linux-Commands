from django.urls import path
from . import views

app_name = 'accounts'
# 회원가입(POST) : account/signup/
# 프로필 정보 조회 및 수정(GET/PUT) : account/user
# 비밀번호 번형(POST) : account/password/change/
# 비밀번호 찾기(POST) : account/password/reset/

urlpatterns = [
    path('<int:user_pk>/profile/', views.profile), # 프로필 조회 및 수정
    # path('signout/', views.signout), # 회원탈퇴
    path('<int:user_pk>/roadmap/', views.user_roadmap), # 사용자 로드맵 조회 및 수정
    path('<int:user_pk>/roadmap/detail/', views.user_roadmap_detail), # 사용자 로드맵 상세 조회(이행 수준)
    path('<int:user_pk>/bookmark/', views.bookmark), # 북마크 조회 및 등록 및 해제
    path('partners/', views.partners), # 개발 동료 찾기
]