from django.urls import path, include
from . import views


app_name = 'ep04'

urlpatterns = [
    path('post/', views.post_list),
]
