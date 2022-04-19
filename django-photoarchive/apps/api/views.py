from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.gallery.models import Photo
from apps.api.serializer import PhotoSerializer

@api_view(['GET'])
def api_photo_list(request):
    photos = Photo.objects.all() # Complex Data
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)

def api_photo(request):
    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)
