from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from blog.models import Blog
from blog.serializers import BlogSerializer


class BlogView(ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.watches += 1
        obj.save()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)


