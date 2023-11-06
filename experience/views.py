# from django.shortcuts import render
from django.http import JsonResponse
# from django.forms.models import model_to_dict
from rest_framework import generics, mixins, status
from rest_framework.response import Response

from rest_framework.parsers import MultiPartParser, FormParser


from experience.models import Experience, gallery
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

    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        # order by start_date
        queryset = self.filter_queryset(
            self.get_queryset()).order_by('-start_date')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # return self.get_paginated_response(serializer.data)
            return Response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        experience_serializer = self.get_serializer(data=request.data)
        # start to add pics and save the experience instance if the isntance is valid
        if experience_serializer.is_valid():
            experience_instance = experience_serializer.save()
            uploaded_images = request.FILES.getlist('gallery')
            # make the gallery instance for each uploaded image
            for uploaded_image in uploaded_images:
                gallery_instance = gallery.objects.create(
                    image=uploaded_image,
                    experience=experience_instance
                )
                gallery_instance.save()
            return Response(
                self.get_serializer(experience_instance).data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                experience_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # delete the gallery instances and file first
        experience_instance = self.get_object()
        gallery_instances = gallery.objects.filter(
            experience=experience_instance)
        for gallery_instance in gallery_instances:
            gallery_instance.image.delete()
            gallery_instance.delete()

        return self.destroy(request, *args, **kwargs)
