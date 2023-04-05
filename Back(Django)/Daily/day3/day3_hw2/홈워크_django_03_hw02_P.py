# 데일리 과제 3-2에서 작성한 모델 Article 모델을 참고하여 작성하시오.

1.
python manage.py makemigrations
python manage.py migrate

2.
article=Article()
article.title='this is title'
article.content='this is content of title'
article.save()