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
        start_year = request.GET.get('start_year')
        photo = photo.filter(year_of_capture__gt=str(int(start_year) - 1))

    if 'end_year' in request.GET and request.GET['end_year'] != "":
        end_year = request.GET.get('end_year')
        photo = photo.filter(year_of_capture__lt=str(int(end_year) + 1))
    
    for i in range(0,5):
        if 'form-' + str(i) + '-tag_name' in request.GET and request.GET['form-' + str(i) + '-tag_name'] != "":
            tag = request.GET.get('form-' + str(i) + '-tag_name')
            photo = photo.filter(tags__tag_name__icontains=tag)

    for i in range(0,5):
        if 'form-' + str(i) + '-person_name' in request.GET and request.GET['form-' + str(i) + '-person_name'] != "":
            person = request.GET.get('form-' + str(i) + '-person_name')
            photo = photo.filter(people__name__icontains=person)

    photo_filter = FilterForm()
    return render(request, 'gallery/gallery.html', {'photo': photo, 'filter': photo_filter})

def upload_photo(request):
    return render(request, 'gallery/upload_photo.html')

def photo(request, photo_id):
    # Если есть фотограафия с требуемым id - показываем её
    # Иначе возвращаем 404
    try:
        photo = Photo.objects.get(pk=photo_id)
        tags = photo.tags.all()
        people = photo.people.all()
        return render(request, 'gallery/photo.html', {'photo': photo, 'tags': tags, 'people': people})
    except Photo.DoesNotExist:
        return error_404(request)