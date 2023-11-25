#!/usr/bin/env python3
from datetime import datetime, timedelta
import requests
import json
API_KEY = "67a6b552015743b1b19d9c5131901e3e"
ALEWIFE_ID = "place-alfcl"
FAWCETT_ID = "2152"
HARVARD_ID = "place-harsq"
DTX_ID = "place-dwnxg"
TMPL_ID = "49001"
BROADWAY_ID = "place-brdwy"



def calculate_transit_time(route):
    total_duration = timedelta(seconds=0)
    for leg in route["legs"]:
        # calculate the total duration as time deltas
        total_duration += leg["duration"]
    # update route dictionary with total duration
    route["duration"] = total_duration
    return


def print_route_steps(route):
    print("\nRoute steps: ")
    for leg in route:
        print(f"- {leg['mode']} to {leg['destination']}")

def get_vehicle_departure(STOP_ID, line, direction, overlap_time):
    # Make a request to the MBTA API to get the status of arrival times at the stop
    headers = {
        "x-api-key": API_KEY
    }
    response = requests.get(
        f"https://api-v3.mbta.com/predictions?filter[stop]={STOP_ID}",
        headers=headers
    )
    upcoming = []
    # Check the response status code
    if response.status_code == 200:
        # Success! Parse the JSON response
        data = json.loads(response.content)
        # for each element in the data array, get only those with relationships.route.data[0].id == line
        for element in data["data"]:
            # check if the element is for the correct direction
            if element["relationships"]["route"]["data"]["id"] == line:
                if element["attributes"]["direction_id"] != direction:
                    continue
                else: 
                    # get the predicted arrival time of when vehicle is predicted to be at the stop
                    departure_time = (element["attributes"]["departure_time"])
                    if ((departure_time is None) or (departure_time == "null")):
                        # skip if null or no departure listed
                        continue
                    else:
                        # otherwise convert to datetime object
                        departure_time = datetime.fromisoformat(departure_time)
                        # append to upcoming_trains list
                        upcoming.append(departure_time)
        # if length of upcoming list is 0, return error
        if len(upcoming) == 0:
            return ("null", "null")
        # sort the upcoming list by soonest departure time
        upcoming.sort()
        # in the upcoming list, find the one with the shortest time difference greater overlap_time
        for departure in upcoming:
            # subtract one minute from departure for a buffer
            departure = departure - timedelta(minutes=1)
            delta = departure - datetime.now(departure.tzinfo)
            if delta > timedelta(minutes=overlap_time):
                #return the arrival time of the soonest departure within overlap_time
                return departure, delta
            else:
                continue
    else:
        return (f"Error: {response.status_code}")

# Define the possible common legs. {mode: str, minutes: int, seconds: int, wait: int}
# current dataset uses median trip time from 10/10/2023 from TransitMatters.org
# Dictionaries can later be updated to include real-time API data for each leg for more accurate results
home_to_alewife = {
    "destination": "Alewife",
    "mode": "walk",
    "duration": timedelta(minutes=16, seconds=30),
}
home_to_concord_opp_fawcett = {
    "destination": "Concord Ave/Fawcett bus stop",
    "mode": "walk",
    "duration": timedelta(minutes=5, seconds=0),
}
concord_opp_fawcett_to_harvard = {
    "destination": "Harvard",
    "mode": "74/78 bus",
    "duration": timedelta(minutes=12, seconds=45),
}
alewife_to_park = {
    "destination": "Park",
    "mode": "Red Line",
    "duration": timedelta(minutes=29, seconds=8),
}
harvard_to_park = {
    "destination": "Park",
    "mode": "Red Line",
    "duration": timedelta(minutes=13, seconds=43),
}
park_to_downtowncrossing = {
    "destination": "Downtown Crossing",
    "mode": "Red Line",
    "duration": timedelta(minutes=0, seconds=45),
}
park_to_templeplace = {
    "destination": "Temple Pl. Bus Stop",
    "mode": "walk",
    "duration": timedelta(minutes=2, seconds=0),
}
templeplace_to_herald = {
    "destination": "Herald St.",
    "mode": "SL5 bus",
    "duration": timedelta(minutes=7, seconds=0),
}
downtowncrossing_to_southstation = {
    "destination": "South Station",
    "mode": "Red Line",
    "duration": timedelta(minutes=0, seconds=45),
}
downtowncrossing_red_to_orange = {
    "destination": "Orange Line - Southbound",
    "mode": "walk",
    "duration": timedelta(minutes=2, seconds=0),
}
downtowncrossing_to_tufts = {
    "destination": "Tufts Medical Center",
    "mode": "Orange Line",
    "duration": timedelta(minutes=1, seconds=45),
}
southstation_to_broadway = {
    "destination": "Broadway",
    "mode": "Red Line",
    "duration": timedelta(minutes=3, seconds=45),
}
tufts_to_inkblock = {
    "destination": "Ink Block",
    "mode": "walk",
    "duration": timedelta(minutes=7, seconds=0),
}
broadway_to_inkblock = {
    "destination": "Ink Block",
    "mode": "walk",
    "duration": timedelta(minutes=13, seconds=0),
}
herald_to_inkblock = {
    "destination": "Ink Block",
    "mode": "walk",
    "duration": timedelta(minutes=2, seconds=0),
}

# alewife based start
route_1 = {
    "legs": [
        home_to_alewife,
        alewife_to_park,
        park_to_downtowncrossing,
        downtowncrossing_to_southstation,
        southstation_to_broadway,
        broadway_to_inkblock,
    ],
    "duration": "0",
}

route_2 = {
    "legs": [
        home_to_alewife,
        alewife_to_park,
        park_to_templeplace,
        templeplace_to_herald,
        herald_to_inkblock,
    ],
    "duration": "0",
}

route_3 = {
    "legs": [
        home_to_alewife,
        alewife_to_park,
        park_to_downtowncrossing,
        downtowncrossing_red_to_orange,
        downtowncrossing_to_tufts,
        tufts_to_inkblock,
    ],
    "duration": "0",
}

# bus based start
route_4 = {
    "legs": [
        home_to_concord_opp_fawcett,
        concord_opp_fawcett_to_harvard,
        harvard_to_park,
        park_to_downtowncrossing,
        downtowncrossing_to_southstation,
        southstation_to_broadway,
        broadway_to_inkblock,
    ],
    "duration": "0",
}

route_5 = {
    "legs": [
        home_to_concord_opp_fawcett,
        concord_opp_fawcett_to_harvard,
        harvard_to_park,
        park_to_templeplace,
        templeplace_to_herald,
        herald_to_inkblock,
    ],
    "duration": "0",
}

route_6 = {
    "legs": [
        home_to_concord_opp_fawcett,
        concord_opp_fawcett_to_harvard,
        harvard_to_park,
        park_to_downtowncrossing,
        downtowncrossing_red_to_orange,
        downtowncrossing_to_tufts,
        tufts_to_inkblock,
    ],
    "duration": "0",
}

if __name__ == "__main__":

    #alewife_train = get_vehicle_departure(ALEWIFE_ID, "Red", direction=0, overlap_time=home_to_alewife["duration"].seconds/60)
    bus74 = get_vehicle_departure(FAWCETT_ID, "74", direction=1, overlap_time=5)
    bus78 = get_vehicle_departure(FAWCETT_ID, "78", direction=1, overlap_time=5)
    #harvard_train = get_vehicle_departure(HARVARD_ID, "Red", direction=0, overlap_time=concord_opp_fawcett_to_harvard["duration"].seconds/60)
    #busSL5 = get_vehicle_departure(TMPL_ID, "749", direction=0, overlap_time=20)
    #orange_train = get_vehicle_departure(DTX_ID, "Orange", direction=0, overlap_time=2)

    #print deaprture times and time differences for each separated by new line
    #print(f"\nThe next Red Line Train from Alewife departs at {alewife_train[0]}, in {alewife_train[1]}.")
    #print(f"\nThe next 74 Bus departs from Concord opp Fawcett at {bus74[0]}, in {bus74[1]}.")
    #print(f"\nThe next 78 Bus departs from Concord opp Fawcett at {bus78[0]}, in {bus78[1]}.")
    #print(f"\nThe next Red Line Train from Harvard departs at {harvard_train[0]}, in {harvard_train[1]}.")
    #print(f"\nThe next SL5 Bus departs from Temple Pl. at {busSL5[0]}, in {busSL5[1]}.")
    #print(f"\nThe next Orange Line Train from Downtown Crossing departs at {orange_train[0]}, in {orange_train[1]}.")

    # Calculate the total transit time for each route.
    routes = [route_1, route_2, route_3, route_4, route_5, route_6]
    for route in routes:
        calculate_transit_time(route)
    
    # Find the route with minimum duration time
    sorted_route = min(routes, key=lambda x: x["duration"])
    min_route = sorted_route["duration"]
    
    # convert seconds to hours, minutes, seconds
    print(f"\nFastest Route Duration is {str(min_route)}")
    
    # calculate the ETA by adding the duration to the current time
    eta = datetime.now() + min_route
    eta = eta.strftime("%I:%M:%S %p")
    print(f"ETA {eta}")
    
    # print the route steps
    print_route_steps(sorted_route["legs"])

    # return 