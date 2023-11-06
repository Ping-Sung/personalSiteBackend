from rest_framework import serializers

from .models import Experience, gallery


class ExperienceSerializer(serializers.ModelSerializer):
    gallery = serializers.SerializerMethodField(read_only=True)
    # categories = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Experience
        fields = [
            'id',
            'title',
            'subtitle',
            'year',
            'description',
            'gallery',
            'urls',
            'skills',
            'start_date',
            'categories',
        ]

    # return the image url for each image in the foreign key gallery
    def get_gallery(self, obj):
        gallery_images = gallery.objects.filter(experience=obj)
        images = []
        for image in gallery_images:
            images.append(image.image.url)
        return images

    # return '' if categories is None
    # def get_categories(self, obj):
    #     if obj.categories is None:
    #         return ''
    #     return obj.categories
