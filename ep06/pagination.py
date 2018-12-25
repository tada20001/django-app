from rest_framework.pagination import PageNumberPagination

# 특정 모델에 대해 페이지 사이즈 커스텀
class PostPageNumberPagination(PageNumberPagination):
    page_size = 2
