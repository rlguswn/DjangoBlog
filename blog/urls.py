from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회 /blog/
    path('', views.PostList.as_view(), name='list'),
    # 글 상세 조회 /blog/detail/<int:pk>/
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='detail'),
    # 글 작성 /blog/write/
    path('write/', views.PostWrite.as_view(), name='write'),
    # 글 수정 /blog/detail/update/<int:pk>/
    path('detail/update/<int:pk>/', views.PostUpdate.as_view(), name='update')
    # 글 삭제 /blog/detail/delete/<int:pk>/
    # path('detail/delete/<int:pk>/', views.PostDelete.as_view(), name='delete')
]