from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class DishAPITests(APITestCase):
    data = {
        'category': 'Тестовая категория',
        'energy': 1337,
        'image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=',
        'name': 'Тестовое блюдо',
        'price': 13.37,
    }

    def setUp(self):
        self.url = reverse('api/dish_list_create')
        super().setUp()

    def test_dish_create_fails(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_dish_create_succeeds(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {settings.API_TOKEN}')
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
