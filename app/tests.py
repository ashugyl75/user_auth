from django.test import TestCase, Client
from django.urls import reverse

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_page_status_code(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)