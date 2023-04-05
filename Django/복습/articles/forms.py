from django import forms
from .models import Article

# Form class
# class ArticleForm(forms.Form):
#     title=forms.CharField(max_length=10)
#     content=forms.CharField(widget=forms.Textarea)

# ModelForm 
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model=Article
        fields='__all__'