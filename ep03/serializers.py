from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# 한 필드에 대한 validation 처리 예 : 보통 모델에 구현하지만....
    def validate_title(self, title):
        if 'django' not in title:
            raise ValidationError('제목에 django를 꼭 포함시켜 주세요.')
        return title

# 여러 필드를 한꺼번에 validation 처리할 때....
    def validate(self, data):
        if len(data['title']) % 2 == 0 or len(data['content']) % 2 == 0:
            raise ValidationError('글자 갯수는 홀수로 지정해 주시기 바랍니다.')
        return data


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']
