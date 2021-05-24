# phone_tracker.py - A simple phone tracker

import sys
import phonenumbers
from phonenumbers import geocoder, carrier


if len(sys.argv) < 2:
    print("Usage: phone_tracker.py +ccxxxxxxxx")
    sys.exit()

input_number = sys.argv[1]

try:
    number = phonenumbers.parse(input_number)
except phonenumbers.phonenumberutil.NumberParseException:
    print("Invalid format")

# validating number
print("Validating ...")
if not phonenumbers.is_possible_number(number):
    print("That's not a possible number")
    sys.exit()

if phonenumbers.is_valid_number(number):
    print("It's a possible number and it is in an assigned exchange")
else:
    print("It's a possible number, but it's not in an assigned exchange")
    print("Do you want to continue? (y/n)")
    response = input()
    if response.lower() == "n":
        print("bye :(")
        sys.exit()

# get region and carrier
region = geocoder.description_for_number(number, "en")
carrier = carrier.name_for_number(number, "en")
print(f"Region: {region}")
print(f"Carrier: {carrier}")
