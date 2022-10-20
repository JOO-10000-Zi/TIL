from cProfile import label
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        labels = {
            'title' : '제목',
            'content' : '내용',
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
