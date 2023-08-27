from django.http import JsonResponse
import json
from diary.models import Diary
# from django.forms.models import model_to_dict
from diary.serializers import DiarySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    try:
        # print(DiarySerializer(instance))
        # print(data)
        # res = model_to_dict(diary, fields=['title','content','date'])
        key = request.GET['diary_ID']
        instance = Diary.objects.get(id=key)
        data = DiarySerializer(instance).data 
        return Response(data, status=200)
    except:
        return Response({'error':'Diary not found'},status=404)

@api_view(['POST'])
def api_create(request, *args, **kwargs):

    serializer = DiarySerializer(data=request.data)
    if serializer.is_valid():
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
    # try:
    #     data = json.loads(request.body)
    #     diary = Diary.objects.create(**data)
    #     return Response({'success':'Diary created'},status=201)
    # except:
    #     return Response({'error':'Diary not created'},status=400)