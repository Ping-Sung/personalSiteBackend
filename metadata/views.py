from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def test(request, *args, **kwargs):
    return JsonResponse({'message': 'Hello World!'}, status=200)
