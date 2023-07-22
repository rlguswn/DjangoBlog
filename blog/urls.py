from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post 기능 url
    # 글 목록 조회 /blog/
    path('', views.PostList.as_view(), name='list'),
    # 글 상세 조회 /blog/detail/<int:pk>/
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='detail'),
    # 글 작성 /blog/write/
    path('write/', views.PostWrite.as_view(), name='write'),
    # 글 수정 /blog/detail/update/<int:pk>/
    path('detail/update/<int:pk>/', views.PostUpdate.as_view(), name='update'),
    # 글 삭제 /blog/detail/delete/<int:pk>/
    path('detail/delete/<int:pk>/', views.PostDelete.as_view(), name='delete'),

    # comment 기능 url
    # 댓글 작성
    path('detail/<int:pk>/comment/write/', views.CommentWrite.as_view(), name='cm-write'),
    # 댓글 삭제
    path('detail/comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='cm-delete'),

    # 카테고리 기능 url
    # 카테고리 작성
    path('detail/<int:pk>/category/update/', views.CategoryUpdate.as_view(), name='cg-update'),
    # 카테고리 삭제
    path('detail/<int:pk>/category/<int:category_pk>/delete/', views.CategoryDelete.as_view(), name='cg-delete'),
    # 카테고리 검색
    path('detail/category/search/', views.CategorySearch.as_view(), name='cg-search'),
]