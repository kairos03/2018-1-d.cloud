from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class UploadFileTestCase(APITestCase):
    def setup(self):
        self.tearDown()

    def tearDown(self):
        pass

    def test_upload(self):
        url = reverse('file-list')
        data = {'object_key': 'test_object_key'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

