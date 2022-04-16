from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.gallery.models import Photo
from apps.gallery.serializer import PhotoSerializer

photo_arr = [
    {'id': 1, 'description': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", 'author': "Author placeholder #1", 'path':'img/photos/1.png'},
    {'id': 2, 'description': "Description placeholder #2", 'author': "Author placeholder #2", 'path':'img/photos/2.png'},
    {'id': 3, 'description': "Description placeholder #3", 'author': "Author placeholder #3", 'path':'img/photos/3.png'},
    {'id': 4, 'description': "Перед началом посвящения ММФ. На фото - ???", 'author': "Пестерев Никита", 'path':'img/photos/4.png'},
    {'id': 5, 'description': "Перед началом посвящения ММФ. На фото сидит ???", 'author': "Пестерев Никита", 'path':'img/photos/5.png'},
]

def gallery(request):
    return render(request, 'gallery/gallery.html')

def photo(request, photo_id):
    #TODO: реализовать передачу данных из БД
    photo = None
    for i in photo_arr:
        if i['id'] == int(photo_id):
            photo = i
    context = {'photo': photo}
    return render(request, 'gallery/photo.html', context)

@api_view(['GET'])
def photo_list(request):
    photos = Photo.objects.all() # Complex Data
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)