from rest_framework import serializers

from apps.gallery.models import Author


class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description = serializers.CharField(label='Описание', allow_blank=False, max_length=280, required=True)
    author = serializers.PrimaryKeyRelatedField(label='Автор', queryset=Author.objects.all())
    publish_date = serializers.DateTimeField(label='Дата публикации')
    hidden = serializers.BooleanField(label='Скрыто')