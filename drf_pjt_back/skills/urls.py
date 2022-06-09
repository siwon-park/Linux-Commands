from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('', views.roadmap), # 로드맵 조회 
    path('<int:skill_pk>/', views.roadmap_detail), # 로드맵 상세 조회
    path('<int:skill_pk>/roadmap/<int:user_pk>/', views.roadmap_pick), # 로드맵 선택(등록)


]