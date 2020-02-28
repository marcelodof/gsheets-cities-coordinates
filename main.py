from services.gsheets_api import get_list
from services.gmaps_api import Geocode

GSHEETS_ID = '17_iZW9DS1MQRTBnRrkBWN-8sMlgTdQx--xh4r96QMlg'
GSHEETS_RANGE = 'A1:A100'

def get_cities_list(id, range):
    """Gets a list of cities from a google sheets."""
    return get_list(id, range)

def get_coordinates(city_list):
    """Gets the coordinates of a city."""
    geo = Geocode()
    results = {}
    for city in city_list:
        coordinates = geo.get_coordinates(city)
        results[city] = str(coordinates['results'][0]['geometry']['lat']) + \
            ', ' + str(coordinates['results'][0]['geometry']['lng'])
    return results

def main():
    """Main Entry Point."""
    city_list = get_cities_list(GSHEETS_ID, GSHEETS_RANGE)
    city_coordinates = get_coordinates(city_list)
    for city, coordinates in city_coordinates.items():
        print(city, ': ', coordinates)

if __name__ == '__main__':
    main()