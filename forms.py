from django import forms
from .models.article import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'author', 
            'date_updated', 
            'topic', 
            'sub_topic', 
            'category', 
            'sub_category',
            'argument',
            'title',
            'paragraphs',
            'status',
            ]
