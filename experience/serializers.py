from rest_framework import serializers

from .models import Experience


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = [
            'id',
            'title',
            'subtitle',
            'company',
            'year',
            'description',
            'gallary',
            'urls',
            'skills',
        ]
