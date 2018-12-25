from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'ep08'

router = DefaultRouter()
router.register('post', views.PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
