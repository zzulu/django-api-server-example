from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def comment_create(request, post_id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user_id=request.user.id, post_id=post_id)
        return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes((JSONWebTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user.id != comment.user.id:
        return Response({'message': 'You are not allowed to delete this Comment.'}, status=status.HTTP_403_FORBIDDEN)
    comment.delete()
    return Response({'id': comment_id})
