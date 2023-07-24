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
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-range', 'placeholder': '댓글을 작성해주세요.'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
