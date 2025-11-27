import unittest
import json
from app import app

class FlaskAppTestCase(unittest.TestCase):
    
    def setUp(self):
        """Configurar el cliente de prueba"""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_endpoint(self):
        """Test del endpoint principal"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Aplicacion creada por Irina', response.data)
        self.assertIn(b'1.0.5', response.data)

    def test_ai_endpoint(self):
        """Test del endpoint de IA"""
        response = self.app.get('/ai')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('ai_response', data)
        self.assertIn('timestamp', data)
        self.assertEqual(data['version'], '1.0.5')
        self.assertEqual(data['author'], 'Irina')

    def test_health_endpoint(self):
        """Test del endpoint de salud"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['version'], '1.0.5')
        self.assertIn('timestamp', data)

    def test_info_endpoint(self):
        """Test del endpoint de información"""
        response = self.app.get('/info')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['version'], '1.0.5')
        self.assertEqual(data['author'], 'Irina')
        self.assertIn('Flask AI App', data['app_name'])

    def test_nonexistent_endpoint(self):
        """Test de endpoint inexistente"""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
