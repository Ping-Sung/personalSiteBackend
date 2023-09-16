from rest_framework import generics, mixins, authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAdminUser
from .models import Diary
from .serializers import DiarySerializer

# generic view is a view that abstracts common patterns when working with views and models.


class DiaryDetailApiView(
    # StaffEditorPermissionsMinxin,
    generics.RetrieveAPIView
):

    # Try to print permission_classes inherited from StaffEditorPermissionsMinxin
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.permission_classes)  # 打印permission_classes

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class DiaryListCreateApiView(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer

    # Both POST and GET requests will pass the permission check.

    # the following permission_classes method is called when a POST request is made.
    # A GET request will not pass the permission check.
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content == None:
            content = title
        serializer.save(content=content)
        print(serializer.validated_data)


class DiaryUpdateApiView(generics.UpdateAPIView):

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    lookup_field = 'pk'


class DiaryDeleteApiView(generics.DestroyAPIView):

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    lookup_field = 'pk'


# mixins class can extend the functionality of a class, so that it can be used in multiple classes.

class DiaryMixinApiView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    # queryset and serializer_class are required for generics.GenericAPIView.
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            # retrieve, list, create ...etc are inherited from mixins.RetrieveModelMixin
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # perform_create is a method that is called when a POST request is made.
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content == None:
            content = title
        serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['GET', 'POST'])
def diary_create_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == 'GET':
        if pk is not None:
            # output one object

            # qs = Diary.objects.filter(id=pk)
            # if not qs.exists():
            #     return Response({'message': 'diary not found.'}, status=404)
            # obj = qs.first()

            # This is the same as the above 4 lines
            obj = get_object_or_404(Diary, id=pk)
            serializer = DiarySerializer(obj)
            return Response(serializer.data, status=200)
        # output all objects
        qs = Diary.objects.all()

        serializer = DiarySerializer(qs, many=True)

        return Response(serializer.data, status=200)

    if method == 'POST':
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content == None:
                content = title

            serializer.save(
                content=content
            )
            print('this is serializer.validated_data')
            return Response(serializer.data, status=201)
        return Response({}, status=400)
