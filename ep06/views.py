from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ep04.models import Post
from ep04.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = super().get_queryset()  # 부모의 queryset을 호출
        qs = qs.filter(title__icontains='team')
        return qs
