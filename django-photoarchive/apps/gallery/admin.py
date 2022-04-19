from django.contrib import admin
from .models import Photo, Tag, Person, Author

# Register your models here.

admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Person)