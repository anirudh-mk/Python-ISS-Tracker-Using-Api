import requests


# for more information about iss tracker api
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/

def iss_near_me(my_latitude, my_longitude):

    url = 'http://api.open-notify.org/iss-now.json'

    # accept response from iss tracker api
    response = requests.get(url=url)

    # Rise error when data is not available
    response.raise_for_status()

    # store data jason data into data
    data = response.json()
    # print(data)

    # iss longitude and latitude
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])

    # print(f"latitude : {latitude}  longitude : {longitude}")

    # if iss is near me with 5 degree deviation
    if my_latitude-5 <= latitude <= my_latitude+5 and my_longitude-5 <= longitude <= my_longitude+5:
        return True
