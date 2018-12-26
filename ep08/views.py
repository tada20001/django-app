from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorUpdateOrReadonly

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [IsAuthorUpdateOrReadonly]
    # permission_classes = [
    #     IsAuthenticated, # AllowAny는 디폴트이므로 인증된 유저만 지정할 시 지정하지 않음
    # ]

    # post 저장시 현재 인증된 유저 저장
    # IP fields 자동 지정
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user, ip=self.request.META['REMOTE_ADDR'])
