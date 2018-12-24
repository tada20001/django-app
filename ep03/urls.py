from django.urls import path, include
from . import views
app_name = 'ep03'

urlpatterns = [
    path('post/', views.PostListAPIView.as_view()),
]
