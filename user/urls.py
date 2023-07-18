from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # User 기능 url
    # 회원가입 /user/register/
    path('register/', views.UserRegister.as_view(), name='register'),
    # 로그인 /user/login/
    path('login/', views.UserLogin.as_view(), name='login'),
    # 로그아웃 /user/logout/
    path('logout/', views.UserLogout.as_view(), name='logout'),
]
