import requests
import datetime


# for more information about sunset and sunrise time api
# https://sunrise-sunset.org/api

def is_night(my_latitude, my_longitude):

    # sunset and sunrise time api parameters
    parameters = {
        'lat': my_latitude,
        'lng': my_longitude,
        'formatted': 0,
    }

    # sunset and sunrise time api
    url = 'https://api.sunrise-sunset.org/json'

    # accept response from sunset and sunrise time api
    response = requests.get(url=url, params=parameters)

    # Rise error when data is not available
    response.raise_for_status()

    # store data jason data into data
    data = response.json()
    # print(data)

    # sun set and sunrise
    sunrise_hour = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset_hour = int(data['results']['sunset'].split('T')[1].split(':')[0])

    # print(f"sunrise : {sunrise_hour} sunset: {sunset_hour}")

    # current Hour
    current_hour = datetime.datetime.now().hour

    if sunset_hour < current_hour < sunrise_hour:
        return True
