from .modules import iss_tarcker, day_or_night
import smtplib
import time

# You can find your longitude and latitude by
# https://www.latlong.net/

# Provide your longitude and latitude here
MY_LATITUDE = 123456
MY_LONGITUDE = 12345

# Enter your email and password
MY_EMAIL = 'axxxxxxx@gmail.com'
MY_PASSWORD = 'xxxxxxxxxx'

# receiver email address
TO_ADDRESS = 'axxxxxxx@gmail.com'

# find iss is near me
iss_near_me = iss_tarcker.iss_near_me(MY_LATITUDE, MY_LONGITUDE)

# ensure day or night in your location
is_night = day_or_night.is_night(MY_LATITUDE, MY_LONGITUDE)

# Run continuously
while True:

    # establish 60sec time interval
    time.sleep(60)

    print("Checking iss is near you............")

    # check it is night or not and iss is near you
    if iss_near_me and is_night:

        # set email protocol
        connection = smtplib.SMTP('smtp.gmail.com')

        # establish connection
        connection.starttls()

        # login to email account
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        # send mail
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_ADDRESS,
                            msg='Subject: Look at the sky /n /n ISS is near You'
                            )



