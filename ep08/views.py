import time
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

    # dispatch time 측정을 위한 코드
    def dispatch(self, request, *args, **kwargs):
        global cbv
        cbv = self

        dispatch_start = time.time()
        response = super().dispatch(request, *args, **kwargs)

        render_start = time.time()
        response.render()
        self.render_time = time.time() - render_start

        self.dispatch_time = time.time() - dispatch_start
        self.api_view_time = self.dispatch_time - (self.render_time + self.serialize_time + self.db_time)

        return response

    # db time, serialize time 측정을 위한 코드

    def list(self, request, *args, **kwargs):
        db_start = time.time()
        post_list = list(self.queryset)  # 현시점에서 즉시 DB fetch
        self.db_time = time.time() - db_start

        serializer_start = time.time()
        serializer = self.get_serializer(self.queryset, many=True)
        data = serializer.data
        self.serializer_time = time.time() - serializer_start

        return Response(data)
