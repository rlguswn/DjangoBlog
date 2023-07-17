from django import forms
from .models import Post, Comment, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']