# pip install phonenumber

import phonenumbers

# geocoder: to know the specific
# location to that phone number

from phonenumbers import geocoder

phone_number = phonenumbers.parse("Phone Number Here") # 👈 paste phone number here

# this will print the country name

print(geocoder.descripton_for_number(phone_number))