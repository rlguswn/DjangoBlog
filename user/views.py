from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from user.forms import RegisterForm, LoginForm, ProfileForm
from blog.forms import CategoryForm
from user.models import User


# Create your views here.
class UserRegister(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')

        register_form = RegisterForm()
        category_form = CategoryForm()
        context = {
            'form': register_form,
            'search_form': category_form
        }
        return render(request, 'user/user_register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            return redirect('user:login')


class UserLogin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')

        login_form = LoginForm
        category_form = CategoryForm()
        context = {
            'form': login_form,
            'search_form': category_form
        }
        return render(request, 'user/user_login.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')

        login_form = LoginForm(request, request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=email, password=password)

            if user:
                login(request, user)
                return redirect('blog:list')

        category_form = CategoryForm()
        login_form.add_error(None, '아이디가 없습니다.')
        context = {
            'form': login_form,
            'search_form': category_form
        }
        return render(request, 'user/user_login.html', context)


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')


class ProfileDetail(View):
    def get(self, request, user):
        user_info = User.objects.get(email=user)
        category_form = CategoryForm()
        context = {
            'user': user_info,
            'search_form': category_form,
        }
        return render(request, 'user/user_profile.html', context)


class ProfileUpdate(View):
    def get(self, request, user):
        user_info = User.objects.get(email=user)
        profile_form = ProfileForm(initial={'image': user_info.image, 'name': user_info.name, 'age': user_info.age})
        category_form = CategoryForm()
        context = {
            'user': user_info,
            'profile_form': profile_form,
            'search_form': category_form
        }
        return render(request, 'user/profile_edit.html', context)

    def post(self, request, user):
        user_info = User.objects.get(email=user)
        profile_form = ProfileForm(request.POST)
        category_form = CategoryForm()

        if profile_form.is_valid():
            user_info.image = profile_form.cleaned_data['image']
            user_info.name = profile_form.cleaned_data['name']
            user_info.age = profile_form.cleaned_data['age']
            user_info.save()
            return redirect('user:p-detail', user=user_info)

        profile_form.add_error(None, '폼이 유효하지 않습니다')
        context = {
            'profile_form': profile_form,
            'search_form': category_form
        }
        return render(request, 'blog/post_form.html', context)