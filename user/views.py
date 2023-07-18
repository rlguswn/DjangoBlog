from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from user.forms import RegisterForm, LoginForm


# Create your views here.
class UserRegister(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')

        register_form = RegisterForm()
        context = {
            'form': register_form
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
        context = {
            'form': login_form
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

        login_form.add_error(None, '아이디가 없습니다.')
        context = {
            'form': login_form
        }
        return render(request, 'user/user_login.html', context)


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')
