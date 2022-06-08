from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    # path('', views.roadmap), # 로드맵 조회 및 선택
    # path('<int:skill_pk>/', views.roadmap_detail), # 로드맵 상세 조회
]