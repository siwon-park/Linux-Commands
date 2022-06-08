from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 전체 게시글 조회 및 단일 게시글 생성
    path('', views.article_list_or_create),
    # 단일 게시글 상세 조회 및 수정, 삭제
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    # 게시글 좋아요 등록 및 해제
    path('<int:article_pk>/like/', views.article_like),
    # 전체 댓글 조회 및 댓글 생성
    path('<int:article_pk>/comment/', views.comment_list_or_create),
    # 단일 댓글 수정 및 삭제
    path('<int:article_pk>/comment/<int:comment_pk>/', views.comment_create_or_update_or_delete),
    # 댓글 좋아요 등록 및 해제
    path('<int:article_pk>/comment/<int:comment_pk>/like/', views.comment_like),
]