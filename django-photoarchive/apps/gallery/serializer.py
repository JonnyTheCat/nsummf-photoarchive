from rest_framework import serializers


class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    description = serializers.CharField(label='Описание', allow_blank=False, max_length=280, required=True)
    author = serializers.CharField(label='Автор', allow_blank=False, max_length=30, required=True)
    publish_date = serializers.DateTimeField(label='Дата публикации')
    hidden = serializers.BooleanField(label='Скрыто')