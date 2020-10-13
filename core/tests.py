import unittest
from django.test import TestCase, Client


class TtsTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_tts(self):
        response = self.client.post('/tts/', {'text': 'hello'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json().get('url'))