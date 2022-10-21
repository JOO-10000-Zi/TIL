from django import forms
from .models import Articles, Comment

class ArticlesForm(forms.ModelForm):
    
    class Meta:
        model = Articles
        fields = ('title', 'content')
        labels = {
            'title': '제목',
            'content': '내용',
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)