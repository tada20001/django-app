from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('ep03/', include('ep03.urls', namespace='ep03')),
    path('ep04/', include('ep04.urls', namespace='ep04')),
    path('ep06/', include('ep06.urls', namespace='ep06')),

]
