from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import views_fbv

app_name = 'ep03'

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('post', views.PostViewSet)


urlpatterns = [
    path('post/', views.PostListAPIView.as_view()),
    path('post/<int:pk>/', views.PostDetailAPIView.as_view()),
    path('', include(router.urls)),

    #path('post/', views_fbv.post_list),

    # path('user/', views.user_list),
    # path('user/<int:pk>/', views.user_detail),  ## 위의 등록된 router가 이러한 url 작업을 대신 해줌
]
