from django.db import models


class Photo(models.Model):
    description = models.CharField("Описание", max_length=255)
    author = models.CharField("Автор", max_length=30)
    hidden = models.BooleanField("Скрыто")
    publish_date = models.DateTimeField(auto_now_add=True)
    year_of_capture = models.SmallIntegerField()
    month_of_capture = models.SmallIntegerField()
    day_of_capture = models.SmallIntegerField()
    view_count = models.IntegerField()

    people = models.ManyToManyField("Person")
    tags = models.ManyToManyField("Tag")

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description

    def image_thumb(self):
        return '<img class="photo-preview" src="/media/photos/%s" width="100%">' % (self.img)


class Profile(models.Model):
    description = models.TextField()
    title_photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Person(models.Model):
    name = models.CharField(max_length=60)
    profile_id = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    pass


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)
    tag_type = models.SmallIntegerField()
    popularity = models.IntegerField()
    profile_id = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    pass

