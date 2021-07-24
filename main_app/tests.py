from django.test import TestCase
from rest_framework.test import APIClient
from time import time


class ApiTests(TestCase):

    test_data = {"links": ["www.somedomain.ru", "http://somedomain2.com"]}
    wrong_test_data = {"links": '''["www.somedomain.ru", http://somedoma'''}
    wrong_test_data2 = {"links1111111111": ["www.somedomain.ru", "http://somedomain2.com"]}

    def test_post_data(self):
        client = APIClient()
        resp = client.post('/api/visited_links/', data=self.test_data, format='json')
        self.assertEqual(resp.status_code, 201)

    def test_get_data(self):
        client = APIClient()
        client.post('/api/visited_links/', data=self.test_data, format='json')
        time_now = str(int(time()))
        resp = client.get(f'/api/visited_domains/?from={time_now}&to={time_now}')
        self.assertEqual(resp.status_code, 200)

    def test_get_without_params(self):
        client = APIClient()
        client.post('/api/visited_links/', data=self.test_data, format='json')
        resp = client.get('/api/visited_domains/')
        self.assertEqual(resp.status_code, 400)

    def test_post_wrong_data(self):
        client = APIClient()
        resp = client.post('/api/visited_links/', data=self.wrong_test_data, format='json')
        self.assertEqual(resp.status_code, 400)

    def test_post_wrong_data2(self):
        client = APIClient()
        resp = client.post('/api/visited_links/', data=self.wrong_test_data2, format='json')
        self.assertEqual(resp.status_code, 400)

