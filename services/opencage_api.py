"""OpenCage API."""
import requests

API_KEY = ''

class Geocode():
    """Geocode API Class."""

    def __init__(self):
        """Init Geocode."""
        self.key = API_KEY
        self.endpoint = 'https://api.opencagedata.com/geocode/v1/json'

    def get_coordinates(self, city):
        """Get coordinates from a city."""
        endpoint = self.endpoint + '?q=' + city \
            + '&key=' + self.key
        response = requests.get(endpoint)
        return response.json()