import unittest
import json
from flask_app import app


class TestSpamChecker(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_spam_checker_valid_input(self):
        data = {'email': 'test@example.com'}
        response = self.app.post('/spamcheck', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('result', response_data)
        self.assertTrue(response_data['result'] in [True, False])

    def test_spam_checker_invalid_input(self):
        data = {}
        response = self.app.post('/spamcheck', json=data)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data)
        self.assertIn('error', response_data)

    def test_spam_checker_empty_email(self):
        data = {'email': ''}
        response = self.app.post('/spamcheck', json=data)
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data)
        self.assertIn('error', response_data)

    def test_spam_email(self):
        data = {
            "email": "Our records show you overpaid for (a product or service). Kindly supply your bank routing and account number to receive your refund."
        }
        response = self.app.post('/spamcheck', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], True)

    def test_not_spam_email(self):
        data = {
            "email": "Hey today we have a meeting, will you join?"
        }
        response = self.app.post('/spamcheck', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], False)


if __name__ == '__main__':
    unittest.main()
