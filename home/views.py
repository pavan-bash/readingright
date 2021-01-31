from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import UserRegisterSerializer
from .models import Post
from django.http import JsonResponse


User = get_user_model()


@api_view(['POST'])
def register_view(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully Created USER"
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.values()
        return JsonResponse(list(posts), safe=False)

    if request.method == "POST":
        return "OK"
