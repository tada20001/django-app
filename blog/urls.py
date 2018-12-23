from django.urls import include, path
from rest_framework.routers import DefaultRouter
#from .views import PostViewSet
from . import views
#router = DefaultRouter()
#router.register(r'post', PostViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('post/', views.PostList.as_view())
]
