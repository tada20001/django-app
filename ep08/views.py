import time
from rest_framework.response import Response
from django.core.signals import request_started, request_finished
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
        self.api_view_time = self.dispatch_time - (self.render_time + self.serializer_time + self.db_time)

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


def started_fn(sender, **kwargs):
    global started
    started = time.time()

def finished_fn(sender, **kwargs):
    request_response_time = (time.time() - started) - cbv.dispatch_time

    total = cbv.db_time + cbv.serializer_time + cbv.api_view_time + cbv.render_time + request_response_time

    print('total                                : {:.6f}s'.format(total))

    print('Database Lookup    - db_time         : {:.6f}s, {:>4.1f}%'.format(cbv.db_time, 100*(cbv.db_time/total)))
    print('Serialization      - serializer_time : {:.6f}s, {:>4.1f}%'.format(cbv.serializer_time, 100*(cbv.serializer_time/total)))
    print('API View           - api_view_time   : {:.6f}s, {:>4.1f}%'.format(cbv.api_view_time, 100*(cbv.api_view_time/total)))
    print('Response rendering - render_time     : {:.6f}s, {:>4.1f}%'.format(cbv.render_time, 100*(cbv.render_time/total)))
    print('Django request/response              : {:.6f}s, {:>4.1f}%'.format(request_response_time, 100*(request_response_time/total)))

request_started.connect(started_fn)    # 요청 처리 시작
request_finished.connect(finished_fn)  # 요청 처리 끝
