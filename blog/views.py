from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm
from .models import Post


# Create your views here.
class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'blog/post_list.html', context)


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        context = {
            'post': post
        }
        return render(request, 'blog/post_detail.html', context)


class PostWrite(View):
    def get(self, request):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html', context)
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog:list')


class PostUpdate(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title':post.title, 'content':post.content})
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)


class PostDelete(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')
