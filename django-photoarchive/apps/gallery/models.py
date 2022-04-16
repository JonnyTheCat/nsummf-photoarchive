from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    
    pass

class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    pass

class Person(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    pass

class Photo(models.Model):
    description = models.CharField("Описание", max_length=280)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    people = models.ManyToManyField(Person)
    publish_date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    hidden = models.BooleanField("Скрыто")

    class Meta:
        ordering = ['description']
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __unicode__(self):
        return self.description
    def __str__(self):
        return self.description
    def image_thumb(self):
        return '<img class="photo-preview" src="/media/photos/%s" width="100%">' % (self.img)
