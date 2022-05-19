from django.contrib import admin
from .models import Photo, Tag, Person, Title, Job

# Register your models here.

admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Person)
admin.site.register(Title)
admin.site.register(Job)