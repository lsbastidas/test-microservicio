import unittest
from flask import Flask
from microservicio import app  # Importa tu app Flask

class TestHola(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hola(self):
        response = self.app.get('/hola')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '¡Hola desde mi microservicio!')

    def test_hola_content_type(self): # Prueba adicional para el Content-Type
        response = self.app.get('/hola')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

if __name__ == '__main__':
    unittest.main()
