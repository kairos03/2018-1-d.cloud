from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from restful.models import File


class FileListTestCase(APITestCase):
      
    def setUp(self):
        self.tearDown()

    def tearDown(self):
        pass

    def test_upload(self):
        url = reverse('file-list')
        data = {'object_key': 'test_object_key'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(File.objects.count(), 1)

    def test_list(self):
        url = reverse('file-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FileDetailTestCase(APITestCase):

    def setUp(self):
        self.tearDown()
        File.objects.create(object_key='test_object')

    def tearDown(self):
        File.objects.all().delete()

    def test_delete(self):
        url = reverse('file-detail', kwargs={'pk' : 1 })
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update(self):
        url = reverse('file-detail', kwargs={'pk' : 1 })
        response = self.client.put(url, {"object_key":"test_update"})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve(self):
        url = reverse('file-detail', kwargs={'pk' : 1 })
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
   