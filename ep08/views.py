from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # post 저장시 현재 인증된 유저 저장
    # IP fields 자동 지정
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user, ip=self.request.META['REMOTE_ADDR'])
