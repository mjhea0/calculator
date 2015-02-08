import unittest
from flask import Flask, current_app

from calculate import app, solve

class CalculatorTests(unittest.TestCase):

    def create_app(self):
        app = Flask(__name__)
        return app

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'Calculator')
    
    def test_main_page_returns_form(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn('<form role="form" method="POST">', response.data)

    def testAdding(self):
        with app.test_request_context:
            result = solve(10, 2)

        self.assertEqual(result, 12)

if __name__ == "__main__":
    unittest.main()