from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)
    else:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
