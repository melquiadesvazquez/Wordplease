import django_filters
from rest_framework import serializers

from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):

    author_fullname = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()

    def get_author_fullname(self, obj):
        return '{0} {1}'.format(obj.author.first_name, obj.author.last_name)

    def get_author_username(self, obj):
        return obj.author.username

    class Meta:

        model = Post
        fields = ['id', 'title', 'description', 'image', 'video', 'author_fullname', 'author_username', 'category', 'pub_date']


class PostSerializer(PostListSerializer):

    class Meta(PostListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['id', 'blog', 'author', 'slug']
