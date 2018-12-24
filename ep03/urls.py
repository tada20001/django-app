from django.urls import path, include
from . import views
from . import views_fbv

app_name = 'ep03'

urlpatterns = [
    #path('post/', views.PostListAPIView.as_view()),
    #path('post/<int:pk>/', views.PostDetailAPIView.as_view()),

    path('post/', views_fbv.post_list),
]
