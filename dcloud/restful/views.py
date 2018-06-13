from django.http import Http404
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from restful import s3_interface

from restful.models import File  
from restful.serializers import FileSerializer  

class FileList(APIView):
    """
    List all file, or create a new snippet.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    """
    list files or view detail
    """
    def get(self, request, path="/", format=None):
        user = request.user
        data = s3_interface.list_path(s3_interface.BUCKET, user.username, path)
        return Response(data)

    """
    upload file
    """
    def post(self, request, path="/", format=None):
        # file upload
        # upload to server
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            # upload to s3
            file_path = '.' + file_serializer.data.get('file')
            user = request.user
            data = s3_interface.upload_file(s3_interface.BUCKET, user.username, file_path, path+file_path.split('/')[-1])
            # TODO upload check
            # TODO remove local file
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """
    make directory
    """
    def put(self, request, path="/", format=None):
        user = request.user
        data = s3_interface.make_directory(s3_interface.BUCKET, user.username, path)
        return Response(data, status=status.HTTP_201_CREATED)

class FileDetail(APIView):
    """
    Download or delete a file instance.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, path="/", format=None):
        # download file from s3
        file = 'media/'+path.split('/')[-1]
        user = request.user
        s3_interface.download_file(s3_interface.BUCKET, user.username, file, path)
        # TODO error
        return Response({'file': file})

    def delete(self, request, path="/", format=None):
        user = request.user
        result = s3_interface.delete_path(s3_interface.BUCKET, user.username, path)
        return Response(result)

class FileCopyMove(APIView):
    """
    Download or delete a file instance.
    """

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    #TODO is folder move, copy well?
    # move
    def post(self, request, old_path, new_path, format=None):
        user = request.user
        if request.data.get('method') == 'mv':
            s3_interface.move_file(s3_interface.BUCKET, user.username, old_path, new_path)
        elif request.data.get('method') == 'cp':
            s3_interface.copy_file(s3_interface.BUCKET, user.username, old_path, new_path)
        else:
            return Response({'stats': 'bad_request'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'old_path': old_path, 'new_path': new_path})


