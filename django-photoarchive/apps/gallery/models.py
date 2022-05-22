from django.db import models
from django.contrib.auth.models import User


TAG_TYPE_CHOICES = [
    (1, 'Места'),
    (2, 'События'),
    (3, 'Другое'),
]


class Photo(models.Model):
    description = models.CharField("Описание", max_length=255, default='Неизвестно', blank=True, null=True)  # Описание
    author = models.CharField("Автор", max_length=30, blank=True, null=True)  # Автор фотографии

    people = models.ManyToManyField("Person", blank=True, null=True)  # Люди на фото
    tags = models.ManyToManyField("Tag", blank=True, null=True)  # Теги

    year_of_capture = models.SmallIntegerField("Год", blank=True, null=True)
    month_of_capture = models.SmallIntegerField("Месяц", blank=True, null=True)  # Год, месяц и день, когда было сделано фото
    day_of_capture = models.SmallIntegerField("День", blank=True, null=True)

    hidden = models.BooleanField("Скрыто")  # Скрыта ли фотография из галереи?

    uploaded_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    publish_date = models.DateTimeField(auto_now_add=True)  # Дата публикации фото на сайте
    view_count = models.IntegerField(default=0, editable=False)  # Счетчик просмотров

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.description


class Person(models.Model):
    name = models.CharField("ФИО", max_length=60)  # Имя человека
    popularity = models.IntegerField(default=0, editable=False)  # Популярность человека на сайте

    # Профиль человека
    # Когда у человека значение has_profile = True, то 
    # создаётся отдельная страница с фотографиями, на которых 
    # отмечен этот человек, а также его биографией.
    has_profile = models.BooleanField("Есть профиль")  # Существует ли профиль?
    date_of_birth = models.DateField("Дата рождения", blank=True, null=True)  # Дата рождения
    date_of_death = models.DateField("Дата смерти", blank=True, null=True)  # ...и смерти (если такая есть)
    description = models.TextField("Описание", blank=True)  # Описание в профиле
    title_photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL)  # Фото профиля

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return self.name


class Title(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    nomination_date = models.SmallIntegerField()

    class Meta:
        verbose_name = 'Титул'
        verbose_name_plural = 'Титулы'

    def __str__(self):
        return f'{self.person_id} - {self.title}'


class Job(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    job = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    started_from = models.SmallIntegerField()

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return f'{self.person_id} - {self.job}'


class Tag(models.Model):
    tag_name = models.CharField("Имя тега", max_length=40)  # Имя тега
    tag_type = models.SmallIntegerField("Тип тега", choices=TAG_TYPE_CHOICES)  # Тип тега
    popularity = models.IntegerField(default=0, editable=False)  # Популярность тега на сайте

    # Профиль тега
    # Когда у тега значение has_profile = True, то как и в Person 
    # создаётся отдельная страница с фотографиями с 
    # этим тегом и описанием этого тега.
    has_profile = models.BooleanField("Есть профиль")  # Существует ли профиль?
    description = models.TextField("Описание", blank=True, null=True)  # Описание в профиле
    title_photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL)  # Фото профиля

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.tag_name
