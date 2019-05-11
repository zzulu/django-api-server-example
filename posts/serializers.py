from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user_name', 'created_at', 'updated_at',)


class PostSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'user_name', 'comments', 'created_at', 'updated_at',)

