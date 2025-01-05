import unittest
from dev.api.add_friend.add_friend_api import app  # Import the  add-event_api.py Flask 

class FlaskAppTestCase(unittest.TestCase):
    
    # Set up the test client
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True  # Enable testing mode for Flask

    # Test the home route
    def test_home(self):
        response = self.app.get('/')  # Make a GET request to the home route
        self.assertEqual(response.status_code, 200)  # Ensure the status code is 200 (OK)
        self.assertEqual(response.data.decode(), "Welcome to the add_friend API!")  # Ensure the response is correct

if __name__ == '__main__':
    unittest.main()
