from django.forms import widgets  
from rest_framework import serializers  
from restful.models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('created', 'updated', 'object_key')
