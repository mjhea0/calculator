import unittest
from flask import Flask, json
from run import app

class CalculatorTests(unittest.TestCase):

    def test_main_page_returns_form(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn('<form role="form" method="POST"', response.data)

    def test_index_get(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Calculator', response.data)

    def test_index_post(self):
        tester = app.test_client(self)
       
        response = tester.post('/',  data={
                'num1': 2,
                'num2': 4,
                'operator': 'add'
            })
        self.assertEqual(json.loads(response.data)['result'], 6)
        self.assertEqual(response.status_code, 200)

        response = tester.post('/',  data={
                'num1': 5,
                'num2': 10,
                'operator': 'multiply'
            })
        self.assertIn('50', response.data)
        self.assertEqual(json.loads(response.data)['result'], 50)
        self.assertEqual(response.status_code, 200)

        response = tester.post('/',  data={
                'num1': 5,
                'num2': 0,
                'operator': 'divide'
            })
        self.assertIn('error', response.data)
        self.assertEqual(response.data, '{"error": "Cannot divide by zero"}')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()