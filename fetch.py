#!/usr/bin/env python3
import requests
import json
from datetime import datetime

'''
# Program: fetch.py
# Author: Jacob Hammond

Structure of the JSON response from the MBTA API:
https://api-v3.mbta.com/vehicles: This is the base URL of the MBTA API endpoint for fetching vehicle data.
filter[stop]={STOP_ID}: This filter specifies that we only want vehicles that are at the specified stop ID.
filter[direction]=inbound: This filter specifies that we only want vehicles that are traveling in the inbound direction.
filter[relationship][type]=trip: This filter specifies that we only want vehicles that are associated with a trip.
filter[relationship][direction]=inbound: This filter specifies that we only want vehicles that are traveling in the inbound direction.
api_key={API_KEY}: This is our API key, which is required for all MBTA API requests.

example: https://api-v3.mbta.com/predictions?include=schedule%2Cstop%2Calerts&filter%5Broute%5D=CR-Fairmount

'''


# Set your API key here
API_KEY = "67a6b552015743b1b19d9c5131901e3e"

# Set the stop ID here
STOP_ID = "2152" # Concord Ave opp Fawcett St bus stop

# Make a request to the MBTA API to get the status of arrival times at the stop
response = requests.get(f"https://api-v3.mbta.com/predictions?filter[stop]={STOP_ID}")

# Check the response status code
if response.status_code == 200:
    # Success! Parse the JSON response
    data = json.loads(response.content)

    # get the predicted arrival time of when vehicle is predicted to be at the stop
    arrival_time= data['data'][0]['attributes']['arrival_time']
    # convert the arrival time to a datetime object in HH:MM:SS format
    arrival_time = datetime.strptime(arrival_time, "%Y-%m-%dT%H:%M:%S-04:00")
    # print the arrival time
    print(f"Arrival time is {arrival_time} ")
    # get the current time
    now = datetime.now()
    # print the current time
    print(f"Current time is {now}")
    # calculate the time difference between the current time and the arrival time
    time_difference = arrival_time - now
    # print the time difference
    print(f"Time difference is {time_difference}")


else:
    # Something went wrong
    print(f"Error: {response.status_code}")