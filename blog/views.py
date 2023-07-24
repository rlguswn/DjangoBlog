from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PostForm, CommentForm, CategoryForm
from .models import Post, Comment, Category


# Create your views here.
class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        category_form = CategoryForm()
        context = {
            'posts': posts,
            'search_form': category_form
        }
        return render(request, 'blog/post_list.html', context)


class PostDetail(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm()
        category_form = CategoryForm()
        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'categories': post.category_set.all(),
            'comment_form': comment_form,
            'category_form': category_form,
            'search_form': category_form
        }
        return render(request, 'blog/post_detail.html', context)


class PostWrite(View):
    def get(self, request):
        post_form = PostForm()
        category_form = CategoryForm()
        context = {
            'post_form': post_form,
            'category_form': category_form,
            'search_form': category_form
        }
        return render(request, 'blog/post_form.html', context)

    def post(self, request):
        post_form = PostForm(request.POST)
        category_form = CategoryForm(request.POST)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.writer = request.user
            post.save()

            if category_form.is_valid():
                category = category_form.cleaned_data['category']
                category_obj = Category.objects.create(category=category)
                category_obj.post.add(post)

            return redirect('blog:list')

        post_form.add_error(None, '폼이 유효하지 않습니다')
        context = {
            'post_form': post_form,
            'category_form': category_form,
            'search_form': category_form
        }
        return render(request, 'blog/post_form.html', context)


class PostUpdate(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post_form = PostForm(initial={'title':post.title, 'content':post.content})
        category_form = CategoryForm()
        context = {
            'form': post_form,
            'post': post,
            'search_form': category_form
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post_form = PostForm(request.POST)
        category_form = CategoryForm()

        if post_form.is_valid():
            post.title = post_form.cleaned_data['title']
            post.content = post_form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)

        post_form.add_error(None, '폼이 유효하지 않습니다')
        context = {
            'form': post_form,
            'search_form': category_form
        }
        return render(request, 'blog/post_form.html', context)


class PostDelete(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')


class CommentWrite(View):
    def post(self, request, pk):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)

        if comment_form.is_valid():
            content = comment_form.cleaned_data['content']
            comment_obj = Comment.objects.create(post=post, content=content)
            return redirect('blog:detail', pk=pk)

        category_form = CategoryForm()
        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'categories': post.category_set.all(),
            'comment_form': comment_form,
            'category_form': category_form,
            'search_form': category_form
        }
        return render(request, 'blog/post_detail.html', context)


class CommentDelete(View):
    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        post_id = comment.post.id
        comment.delete()
        return redirect('blog:detail', pk=post_id)


class CategoryUpdate(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        category_form = CategoryForm()
        context = {
            'post': post,
            'form': category_form,
            'categories': post.category_set.all(),
            'search_form': category_form
        }
        return render(request, 'blog/category_edit.html', context)

    def post(self, request, pk):
        category_form = CategoryForm(request.POST)
        post = Post.objects.get(pk=pk)

        if category_form.is_valid():
            category = category_form.cleaned_data['category']
            category_obj = Category.objects.create(category=category)
            category_obj.post.add(post)
            return redirect('blog:cg-update', pk=pk)

        context = {
            'post': post,
            'categories': post.category_set.all(),
            'category_form': category_form,
            'search_form': category_form
        }
        return render(request, 'blog/category_edit.html', context)


class CategoryDelete(View):
    def post(self, request, pk, category_pk):
        post = Post.objects.get(pk=pk)
        category = Category.objects.get(pk=category_pk)
        category.post.remove(post)
        return redirect('blog:cg-update', pk=post.pk)


class CategorySearch(View):
    def get(self, request):
        category_form = CategoryForm(request.GET)

        if category_form.is_valid():
            category = category_form.cleaned_data['category']
            posts = Post.objects.filter(category__category=category)
        context = {
            'posts': posts,
            'category_form': category_form,
            'search_form': category_form
        }
        return render(request, 'blog/post_list.html', context)
