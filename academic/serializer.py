from rest_framework import serializers

from .models import Academic


class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic
        fields = '__all__'
