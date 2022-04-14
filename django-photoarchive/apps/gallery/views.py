from django.shortcuts import render

photo_arr = [
    {'id': 1, 'description': "Description placeholder #1", 'author': "Author placeholder #1", 'path':'img/photos/1.png'},
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