#!/usr/bin/env python3
from datetime import datetime, timedelta

def calculate_transit_time(route):
    total_duration = 0
    for leg in route["legs"]:
        duration_in_minutes = leg["minutes"]
        duration_in_seconds = leg["seconds"]
        dwell_time_in_seconds = leg["dwell"]
        #calculate the total duration in seconds
        total_duration += duration_in_minutes * 60 + duration_in_seconds + dwell_time_in_seconds
    # update route dictionary with total duration
    route["duration"] = total_duration
    return

def print_route_steps(route):
    for leg in route:
        print(f"{leg['mode']} to {leg['destination']}") 

# Define the possible common legs. {mode: str, minutes: int, seconds: int, dwell: int}
# current dataset uses median trip time from 10/10/2023 from TransitMatters.org 
# Dictionaries can later be updated to include real-time API data for each leg for more accurate results
home_to_alewife = {"destination": "Alewife", "mode": "walk", "minutes": 18, "seconds": 0, "dwell": 60}
home_to_concord_opp_fawcett = {"destination": "Concord Ave Opp Fawcett", "mode": "walk", "minutes": 5, "seconds": 0, "dwell": 60}
concord_opp_fawcett_to_harvard = {"destination": "Harvard", "mode": "bus", "minutes": 12, "seconds": 0, "dwell": 60}
alewife_to_davis = {"destination": "Davis", "mode": "subway", "minutes": 5, "seconds": 11, "dwell": 0}
davis_to_porter = {"destination": "Porter", "mode": "subway", "minutes": 3, "seconds": 56, "dwell": 75}
porter_to_harvard = {"destination": "Harvard", "mode": "subway", "minutes": 2, "seconds": 45, "dwell": 50}
harvard_to_central = {"destination": "Central", "mode": "subway", "minutes": 4, "seconds": 58, "dwell": 91}
central_to_kendall = {"destination": "Kendall/MIT", "mode": "subway", "minutes": 2, "seconds": 6, "dwell": 64}
kendall_to_charles = {"destination": "Charles/MGH", "mode": "subway", "minutes": 1, "seconds": 9, "dwell": 59}
charles_to_park = {"destination": "Park St.", "mode": "subway", "minutes": 1, "seconds": 58, "dwell": 61}
park_to_downtowncrossing = {"destination": "Downtown Crossing", "mode": "subway", "minutes": 0, "seconds": 44, "dwell": 90}
park_to_templeplace = {"destination": "Temple Pl.", "mode": "walk", "minutes": 2, "seconds": 0, "dwell": 30}
templeplace_to_herald = {"destination": "Herald St.", "mode": "bus", "minutes": 7, "seconds": 0, "dwell": 0}
downtowncrossing_to_southstation = {"destination": "South Station", "mode": "subway", "minutes": 0, "seconds": 46, "dwell": 85}
downtowncrossing_red_to_orange = {"destination": "Orange Line - Southbound", "mode": "walk", "minutes": 2, "seconds": 0, "dwell": 0}
downtowncrossing_to_tufts = {"destination": "Tufts Medical Center", "mode": "subway", "minutes": 1, "seconds": 40, "dwell": 55}
southstation_to_broadway = {"destination": "Broadway", "mode": "subway", "minutes": 3, "seconds": 44, "dwell": 16}
tufts_to_inkblock = {"destination": "Ink Block", "mode": "walk", "minutes": 7, "seconds": 0, "dwell": 0}
broadway_to_inkblock = {"destination": "Ink Block", "mode": "walk", "minutes": 13, "seconds": 0, "dwell": 0}
herald_to_inkblock = {"destination": "Ink Block", "mode": "walk", "minutes": 2, "seconds": 0, "dwell": 0}

# alewife based start
route_1 = {"legs": [home_to_alewife, 
           alewife_to_davis, 
           davis_to_porter, 
           porter_to_harvard, 
           harvard_to_central, 
           central_to_kendall, 
           kendall_to_charles, 
           charles_to_park, 
           park_to_downtowncrossing, 
           downtowncrossing_to_southstation, 
           southstation_to_broadway, 
           broadway_to_inkblock],
           "duration":"0"}

route_2 = {"legs": [home_to_alewife,
           alewife_to_davis,
           davis_to_porter,
           porter_to_harvard,
           harvard_to_central,
           central_to_kendall,
           kendall_to_charles,
           charles_to_park,
           park_to_templeplace,
           templeplace_to_herald,
           herald_to_inkblock],
            "duration":"0"}

route_3 = {"legs": [home_to_alewife,
            alewife_to_davis,
            davis_to_porter,
            porter_to_harvard,
            harvard_to_central,
            central_to_kendall,
            kendall_to_charles,
            charles_to_park,
            park_to_downtowncrossing,
            downtowncrossing_red_to_orange,
            downtowncrossing_to_tufts,
            tufts_to_inkblock],
            "duration":"0"}

# bus based start
route_4 = {"legs":[home_to_concord_opp_fawcett,
            concord_opp_fawcett_to_harvard,
            harvard_to_central,
            central_to_kendall,
            kendall_to_charles,
            charles_to_park,
            park_to_downtowncrossing,
            downtowncrossing_to_southstation,
            southstation_to_broadway,
            broadway_to_inkblock],
            "duration":"0"}

route_5 = {"legs": [home_to_concord_opp_fawcett,
            concord_opp_fawcett_to_harvard,
            harvard_to_central,
            central_to_kendall,
            kendall_to_charles,
            charles_to_park,
            park_to_templeplace,
            templeplace_to_herald,
            herald_to_inkblock],
            "duration":"0"}

route_6 = {"legs": [home_to_concord_opp_fawcett,
            concord_opp_fawcett_to_harvard,
            harvard_to_central,
            central_to_kendall,
            kendall_to_charles,
            charles_to_park,
            park_to_downtowncrossing,
            downtowncrossing_red_to_orange,
            downtowncrossing_to_tufts,
            tufts_to_inkblock],
            "duration":"0"}

# Calculate the total transit time for each route.
calculate_transit_time(route_1)
calculate_transit_time(route_2)
calculate_transit_time(route_3)
calculate_transit_time(route_4)
calculate_transit_time(route_5)
calculate_transit_time(route_6)

# Find the route with minimum duration time
routes = [route_1, route_2, route_3, route_4, route_5, route_6]
min_route = min(routes, key=lambda x: x["duration"])
min_route_duration = {min_route['duration']}

#convert seconds to hours, minutes, seconds
hours = min_route['duration'] // 3600
minutes = (min_route['duration'] % 3600) // 60
seconds = (min_route['duration'] % 3600) % 60
print(f"\nFastest Route Duration is {hours}:{minutes}:{seconds}")

# calculate the ETA by adding the duration to the current time
eta = datetime.now() + timedelta(seconds=min_route['duration'])
eta = eta.strftime("%I:%M:%S %p")
print (f"ETA {eta}")

# print the route steps
print("\nRoute steps: ")
print_route_steps(min_route["legs"])

    