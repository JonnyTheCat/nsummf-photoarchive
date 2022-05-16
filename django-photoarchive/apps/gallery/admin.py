from django.contrib import admin
from .models import Photo, Tag, Person, Title, Job

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ('tag_name', 'tag_type')
            }),
        ('Информация для профиля:', {
            'classes': ('collapse',),
            'fields': ('has_profile', 'description', 'title_photo')
            })
    ]

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('name',)}),
        ('Информация для профиля:', {'classes': ('collapse',), 'fields': ('has_profile', 'date_of_birth', 'date_of_death', 'description', 'title_photo')})
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = [
        ('Основная информация', {'classes': ('collapse',), 'fields': ('author', 'description', 'day_of_capture', 'month_of_capture', 'year_of_capture')}),
        ('Теги и люди на фото', {'classes': ('collapse',), 'fields': ('people', 'tags')}),
    ]
    list_display = ("description", "year_of_capture", "id")
    list_filter = ("year_of_capture", "tags", "people")