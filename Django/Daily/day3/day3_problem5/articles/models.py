from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=15)
    content=models.TextField()
    memo=models.CharField(max_length=15, default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.pk}번글 - {self.title} : {self.content} / {self.memo}'