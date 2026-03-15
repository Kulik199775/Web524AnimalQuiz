from rest_framework.test import APITestCase
from rest_framework import status

from sections.tests.utils import get_admin_user, get_member_user, get_test_content


class ContentTestAdmin(APITestCase):
    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_content = get_test_content()

    def test_08_content_create(self):
        data = {
            'section': self.test_content.section.id,
            'title': 'Test Content Title Create',
            'content': 'Test Content Create',
        }
        response = self.client.post('/content/create/', data=data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), 'Test Content Title Create')
        self.assertEqual(response.json().get('content'), 'Test Content Create')

    def test_09_content_detail(self):
        response = self.client.get(f'/content/{self.test_content.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Title Content')
        self.assertEqual(response.json().get('content'), 'Test Content')

    def test_10_content_update(self):
        data = {
            'title': 'Test Title Content PATCH',
        }
        response = self.client.patch(f'/content/{self.test_content.id}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Title Content PATCH')

    def test_11_content_delete(self):
        response = self.client.delete(f'/content/{self.test_content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.delete(f'/content/{self.test_content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_12_content_list(self):
        response = self.client.get('/content/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.json())
        self.assertEqual(response.json()['results'][0]['title'], 'Test Title Content')


class ContentTestMember(APITestCase):
    def setUp(self):
        self.user = get_member_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_content = get_test_content()

    def test_13_content_create_forbidden(self):
        data = {
            'section': self.test_content.section.id,
            'title': 'Test Content Title Create',
            'content': 'Test Content Create',
        }
        response = self.client.post('/content/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # print(response.json())
        self.assertEqual(response.json().get('detail'), 'У вас недостаточно прав для выполнения данного действия.')

    def test_14_content_delete_forbidden(self):
        response = self.client.delete(f'/content/{self.test_content.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # print(response.json())
        self.assertEqual(response.json().get('detail'), 'You are not a superuser.')
