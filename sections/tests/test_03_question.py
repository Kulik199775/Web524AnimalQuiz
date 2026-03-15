from rest_framework.test import APITestCase
from rest_framework import status

from sections.tests.utils import get_test_question, get_member_user


class QuestionTestAdmin(APITestCase):
    def setUp(self):
        self.user = get_member_user()
        response = self.client.post('/users/token/', {'email': self.user.email, 'password': 'qwerty'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.question = get_test_question()

    def test_15_question_list(self):
        response = self.client.get('/question/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.json())
        self.assertEqual(response.json()['results'][0]['question'], 'Test Question')

    def test_16_question_detail(self):
        response = self.client.get(f'/question/{self.question.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['question'], 'Test Question')

    def test_17_question_is_correct(self):
        correct_answer = self.question.answer.title

        answer = {
            'member_answer': 'Test Title Content',
        }
        answer_wrong = {
            'member_answer': 'Wrong Title Content',
        }
        response = self.client.post(f'/question/{self.question.id}/', answer, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('is_correct'), True)

        response = self.client.post(f'/question/{self.question.id}/', answer_wrong, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('is_correct'), False)
