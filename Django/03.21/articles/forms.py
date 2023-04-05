from django import forms
from .models import Article

# Form class
# class ArticleForm(forms.Form):
#     title=forms.CharField(max_length=10)
#     content=forms.CharField(widget=forms.Textarea)

# Model Form
class ArticleForm(forms.ModelForm):
    
    class Meta:
        model=Article
        #Article의 모든 값에 대해서 form을 만들어라
        fields='__all__'
    
    # def clean_title(self):
    #     title=self.cleaned_data('title')
    #     if 'django' in title:
    #         return False
    #     return True