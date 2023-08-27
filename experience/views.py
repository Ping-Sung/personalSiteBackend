# from django.shortcuts import render
from django.http import JsonResponse
# from django.forms.models import model_to_dict
from rest_framework import generics, mixins

from experience.models import Experience
from experience.serializers import ExperienceSerializer

# Create your views here.


# def test(request, *args, **kwargs):
#     instance = Experience.objects.first()
#     data = {}
#     if instance:
#         data = ExperienceSerializer(instance).data

#     return JsonResponse(data)
class ExperienceMixinApiView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    # queryset and serializer_class are required for generics.GenericAPIView.
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # # perform_create is a method that is called when a POST request is made.
    # def perform_create(self, serializer):
    #     title = serializer.validated_data.get('title')
    #     content = serializer.validated_data.get('content') or None
    #     if content == None:
    #         content = title
    #     serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
