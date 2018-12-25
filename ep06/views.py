from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from ep04.models import Post
from ep04.serializers import PostSerializer
from .pagination import PostPageNumberPagination



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['title']


# 실제 search 기능을 구현하면 다음과 같음
'''
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            qs = qs.filter(title__icontains=search)'''

    # def get_queryset(self):
    #     qs = super().get_queryset()  # 부모의 queryset을 호출
    #     if self.request.user.is_authenticated:
    #         qs = qs.filter(author=self.request.user)
    #     else:
    #         qs = qs.none() # empty result
    #     return qs
