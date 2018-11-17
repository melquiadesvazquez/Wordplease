from rest_framework import serializers

from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ['id', 'title', 'description', 'image']


class PostSerializer(PostListSerializer):

    class Meta(PostListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['author']