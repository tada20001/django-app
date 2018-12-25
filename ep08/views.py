from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # IP fields 자동 지정
    def perform_create(self, serializer):
        serializer.save(ip=self.request.META['REMOTE_ADDR'])
