from rest_framework import serializers
from .models import Diary
from rest_framework.reverse import reverse

class DiarySerializer(serializers.ModelSerializer):
    combination = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='diary-detail',
        lookup_field='pk'
    )
    delete_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Diary
        fields = [
            'id',
            'title',
            'content',
            'date', 
            'combination',
            'url',
            'delete_url',

        ]

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def get_delete_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('diary-delete', kwargs={'pk': obj.pk}, request=request)


    def get_combination(self, obj):
        try:
            return obj.title + ": " + obj.content
        except:
            return None