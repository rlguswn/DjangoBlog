from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm, CommentForm
from .models import Post, Comment


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

        comments = post.comment_set.all()
        comment_form = CommentForm()

        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form
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
        form.add_error(None, '폼이 유효하지 않습니다')
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html')


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
        form.add_error(None, '폼이 유효하지 않습니다')
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html', context)


class PostDelete(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')


class CommentWrite(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)
        if form.is_valid():
            content = form.cleaned_data['content']
            comment = Comment.objects.create(post=post, content=content)
            return redirect('blog:detail', pk=pk)

        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'comment_form': form
        }
        return render(request, 'blog/post_detail.html', context)


class CommentDelete(View):
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        post_id = comment.post.id
        comment.delete()
        return redirect('blog:detail', pk=post_id)
