import requests

def test_home_route():
    # Send a GET request to your Flask API home route
    response = requests.get('http://localhost:5004/')  

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check that the response body contains the expected message
    assert response.text == "Welcome to the add_event API!"

# Run the test
if __name__ == "__main__":
    test_home_route()
