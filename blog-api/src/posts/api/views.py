from django.db.models import Q
from rest_framework.filters import(
        SearchFilter,
        OrderingFilter,
)
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView,
    ListCreateAPIView, RetrieveUpdateAPIView)
from posts.models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import(
        PostDetailSerializer,
        PostListSerializer,
        PostCreateUpdateSerializer,)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination


class PostCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]
    #lookup_field = 'slug'
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = "abc"
    #def perform_update(self, serializer):
        #serializer.save(user=self.request.user)

class PostUpdateAPIView(RetrieveUpdateAPIView):
        queryset = Post.objects.all()
        serializer_class = PostCreateUpdateSerializer
        lookup_field = 'slug'
        permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
        def perform_update(self, serializer):
            serializer.save(user=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title','content','user__first_name']
    pagination_class = PostPageNumberPagination #PostLimitOffsetPagination
    #lookup_field = 'slug'
    def get_queryset(self,*args,**kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(args*,**kwargs)
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
        			Q(title__icontains=query)|
        			Q(content__icontains=query)|
        			Q(user__first_name__icontains=query) |
        			Q(user__last_name__icontains=query)
        			).distinct()
        return queryset_list
