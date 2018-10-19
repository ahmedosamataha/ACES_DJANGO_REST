from rest_framework.serializers import (ModelSerializer,
HyperlinkedIdentityField,SerializerMethodField)
from posts.models import Post





class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
    view_name = 'posts-api:detail',
    lookup_field = 'slug'
    )
    user = SerializerMethodField()
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    # delete_url = HyperlinkedIdentityField(
    # view_name = 'posts-api:delete',
    # lookup_field = 'slug'
    # )
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'slug',
            'content',
            'markdown',
            'publish',
            'image',
            #'id'
            #'delete_url',
        ]
    def get_markdown(self,obj):
        return obj.get_markdown()
    def get_user(self,obj):
        return str(obj.user.username)
    def get_image(self,obj):
        try:
            image=obj.image.url
        except:
            image=None
        return image

class PostDetailSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
    view_name = 'posts-api:detail',
    lookup_field = 'slug'
    )
    user = SerializerMethodField()
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    # delete_url = HyperlinkedIdentityField(
    # view_name = 'posts-api:delete',
    # lookup_field = 'slug'
    # )
    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'slug',
            'content',
            'markdown',
            'publish',
            'image',
            #'id'
            #'delete_url',
        ]
    def get_markdown(self,obj):
        return obj.get_markdown()
    def get_user(self,obj):
        return str(obj.user.username)
    def get_image(self,obj):
        try:
            image=obj.image.url
        except:
            image=None
        return image
class PostCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'title',
            #'slug',
            'content',
            'publish'
            #'id'

        ]
# data = {
#     "title": "yeah buddy",
#     "content": "new content",
#     "publish": "2016-2-12",
#     "slug" : "yeah-buddy",
#
# }
# obj = Post.objects.get(id=2)
# new_item = PostDetailSerializer(obj, data=data)
# if new_item.is_valid():
#     new_item.save()
# else:
#     print(new_item.errors)
#
# obbj.delete()
# obj = post.objects.get(id=2)
