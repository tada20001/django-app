from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)
print(router.urls)

app_name = 'ep04'

urlpatterns = [
    path('post/', views.post_list),
    path('post/<int:pk>/', views.post_detail),

    path('api/', include(router.urls)),  # /ep04/api/post
]
