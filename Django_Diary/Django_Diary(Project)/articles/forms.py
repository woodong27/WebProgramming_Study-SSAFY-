from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model=Article
        # fields=('title',)
        fields='__all__'