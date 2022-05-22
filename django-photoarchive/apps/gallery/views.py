from django.shortcuts import render
from .models import Photo, Tag
from .fields import FilterForm

def error_404(request):
    response = render(request, 'base/404_error.html')
    response.status_code = 404
    return response

def gallery(request):
    photo = Photo.objects.all()


    if 'author' in request.GET and request.GET['author'] != "":
        author = request.GET.get('author')
        photo = photo.filter(author__icontains=author)

    if 'start_year' in request.GET and request.GET['start_year'] != "":
        author = request.GET.get('start_year')
        photo = photo.filter(year_of_capture__gt=str(int(author) - 1))

    if 'author' in request.GET and request.GET['end_year'] != "":
        author = request.GET.get('end_year')
        photo = photo.filter(year_of_capture__lt=str(int(author) + 1))

    photo_filter = FilterForm()
    return render(request, 'gallery/gallery.html', {'photo': photo, 'filter': photo_filter})

def upload_photo(request):
    return render(request, 'gallery/upload_photo.html')

def photo(request, photo_id):
    # Если есть фотограафия с требуемым id - показываем её
    # Иначе возвращаем 404
    try:
        photo = Photo.objects.get(pk=photo_id)
        return render(request, 'gallery/photo.html', {'photo': photo})
    except Photo.DoesNotExist:
        return error_404(request)