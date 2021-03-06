from rest_framework import serializers

from blogs.models import Blog
from posts.models import Post


class BlogListSerializer(serializers.ModelSerializer):

    owner_fullname = serializers.SerializerMethodField()
    owner_username = serializers.SerializerMethodField()
    post_count = serializers.SerializerMethodField()

    def get_owner_fullname(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)

    def get_owner_username(self, obj):
        return obj.owner.username

    def get_post_count(self, obj):
        return Post.objects.all().filter(blog=obj.id).count()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'owner_fullname', 'owner_username', 'post_count']


class BlogSerializer(BlogListSerializer):

    class Meta(BlogListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['id', 'owner', 'slug']
