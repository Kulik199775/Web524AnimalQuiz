from rest_framework.test import APITestCase
from rest_framework import status

from sections.tests.utils import get_admin_user, get_member_user, get_test_section


class SectionsTestAdmin(APITestCase):
    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = get_test_section()

    def test_01_section_creation(self):
        data = {
            'title': 'Test Section Create',
            'description': 'Test description Create',
        }
        response = self.client.post('/section/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), 'Test Section Create')

    def test_02_section_detail(self):
        response = self.client.get(f'/section/{self.test_section.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Section')
        self.assertEqual(response.json().get('description'), 'Test description')

    def test_03_section_update(self):
        data = {
            'title': 'Test Section Update PUT',
            'description': 'Test description Update PUT',
        }
        response = self.client.put(f'/section/{self.test_section.id}/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Section Update PUT')
        self.assertEqual(response.json().get('description'), 'Test description Update PUT')

    def test_04_section_delete(self):
        response = self.client.delete(f'/section/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.delete(f'/section/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_05_section_list(self):
        response = self.client.get('/section/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.json())
        self.assertEqual(response.json()['results'][0]['title'], 'Test Section')


class SectionsTestMember(APITestCase):
    def setUp(self):
        self.user = get_member_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'},
                                    format='json')
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = get_test_section()

    def test_06_section_create_forbidden(self):
        data = {
            'title': 'Test Section Create Forbidden',
            'description': 'Test description Create Forbidden',
        }
        response = self.client.post('/section/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), 'У вас недостаточно прав для выполнения данного действия.')

    def test_07_section_delete_forbidden(self):
        response = self.client.delete(f'/section/{self.test_section.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json().get('detail'), 'You are not a superuser.')
