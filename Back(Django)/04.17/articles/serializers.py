from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        # 댓글 생성시 article은 직접 추가하는게 아니기 때문에 read_only_fields로 설정해줌
        read_only_fields=('article',)
    
    def to_representation(self, instance):
        rep=super().to_representation(instance)
        rep.pop('article',None)
        return rep

class ArticleListSerializer(serializers.ModelSerializer):
    # 역참조에 사용할 comment_set 정의(역참조 매니저 이름 그대로 사용하면 됨, 만약 related_name으로 변경해줬다면 그거 사용)
    # comments=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # comment_count라는 걸 추가해서 게시글에 달린 댓글의 수를 가져옴
    # comment_count=serializers.IntegerField(source='comments.count', read_only=True)
    # comments를 불러오면 pk말고 commentserializer를 사용한 데이터를 불러오도록 설정
    # serializer를 중첩시켜주는 것을 nested serializer라고 함
    # comments=CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
        # fields='__all__'
    # 역직렬화, 역참조시 또는 many=True 일때는 read_only_fields에 추가하는게 아니라
    # 옵션에 바로 read_only=True를 걸어줘야 함
    
    # to_representation을 사용해서 직렬화 할 때 보여지는 매니저 명을 바꿔줄 수 있음
    # def to_representation(self, instance):
    #     rep=super().to_representation(instance)
    #     rep['comment_set']=rep.pop('comments',[])
    #     return rep

# 클래스 상속을 통해서 게시글 상세조회시 사용할 클래스를 따로 만들어서 사용할 수 있음
class ArticleDetailSerializer(ArticleListSerializer):
    comments=CommentSerializer(many=True, read_only=True)
    comment_count=serializers.IntegerField(source='comments.count', read_only=True)
    
    class Meta(ArticleListSerializer.Meta):
        fields=ArticleListSerializer.Meta.fields+('comments', 'comment_count',)
    