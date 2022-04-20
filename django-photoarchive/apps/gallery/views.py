from django.shortcuts import render
from .models import Photo

def error_404(request):
    response = render(request, 'base/404_error.html')
    response.status_code = 404
    return response

def gallery(request):
    return render(request, 'gallery/gallery.html')

def photo(request, photo_id):
    try:
        photo = Photo.objects.get(pk=photo_id)
        return render(request, 'gallery/photo.html', {'photo': photo})
    except Photo.DoesNotExist:
        return error_404(request)