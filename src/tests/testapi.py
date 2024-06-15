import unittest
import requests
import yaml

class MyTestCase(unittest.TestCase):
    def test_api_response(self):
        with open("src/config.yml", 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)
        host = cfg['HOST'] if cfg['HOST'] != '0.0.0.0' else 'localhost'
        url = f"http://{host}:{cfg['PORT']}/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Hello, World!')
        
if __name__ == "__main__":
    unittest.main()
