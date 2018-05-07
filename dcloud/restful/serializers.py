from django.forms import widgets  
from rest_framework import serializers  
from restful.models import File


class FileSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(max_length=100)
    object_key = serializers.CharField(max_length=1025)
    size = serializers.IntegerField()


    def create(self, validated_data):
        """
        Create and Return new `File` instance. Using validated_data.
        """
        return File.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and Return existing `File` instance. Using validated_data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.object_key = validated_data.get('object_key', instance.object_key)
        instance.size = validated_data.get('size', instance.size)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
