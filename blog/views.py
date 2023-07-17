from django.shortcuts import render
from django.views import View
from .models import Post


# Create your views here.
class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'blog/post_list.html', context)


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        context = {
            'post': post
        }
        return render(request, 'blog/post_detail.html', context)