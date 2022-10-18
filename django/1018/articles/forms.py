from django import forms
from .models import Article

class ArticleForm(forms.MoedelForm):

    class Meta:
        model = Article
        fields = '__all__'