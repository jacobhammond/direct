import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
#import http.server
#import socketserver

API_KEY = "67a6b552015743b1b19d9c5131901e3e"


def eta(destination, depart_time):
    # set depart_time hour and minute
    depart_time = depart_time.split(":")
    hour = depart_time[0]
    minute = depart_time[1]
    AM_PM = depart_time[2]
    # Get the current time
    now = datetime.now()
    # Get the current year, month, day, hour, minute, and AM/PM
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    # Convert minute to integer
    minute = int(minute)
    # Round up to the next 5-minute interval and account for hour change if necessary
    if minute % 5 != 0:
        minute = minute + (5 - (minute % 5))
        if minute == 60:
            minute = 0
            hour = int(hour)
            hour = hour + 1
            if hour == 13:
                hour = 1
    # Convert minute back to string
    minute = str(minute).zfill(2)

    # URL of the webpage to scrape
    if destination == "ink":
        # Home to Ink Block
        url = f"https://www.mbta.com/trip-planner?plan%5Bfrom%5D=Concord+Ave+opp+Fawcett+St&plan%5Bfrom_latitude%5D=42.389131&plan%5Bfrom_longitude%5D=-71.146219&plan%5Bto%5D=300+Harrison+Avenue%2C+Boston%2C+MA%2C+02118%2C+USA&plan%5Bto_latitude%5D=42.346040742633&plan%5Bto_longitude%5D=-71.062462102185&plan%5Btime%5D=depart&plan%5Bdate_time%5D%5Bhour%5D={hour}&plan%5Bdate_time%5D%5Bminute%5D={minute}&plan%5Bdate_time%5D%5Bam_pm%5D={AM_PM}&plan%5Bdate_time%5D%5Bmonth%5D={month}&plan%5Bdate_time%5D%5Bday%5D={day}&plan%5Bdate_time%5D%5Byear%5D={year}&plan%5Bmodes%5D%5Bsubway%5D=false&plan%5Bmodes%5D%5Bsubway%5D=true&plan%5Bmodes%5D%5Bcommuter_rail%5D=false&plan%5Bmodes%5D%5Bbus%5D=false&plan%5Bmodes%5D%5Bbus%5D=true&plan%5Bmodes%5D%5Bferry%5D=false&plan%5Boptimize_for%5D=best_route#plan_result_focus"
    elif destination == "park":
        # Home to Park Street
        url = f"https://www.mbta.com/trip-planner?plan%5Bfrom%5D=Concord+Ave+opp+Fawcett+St&plan%5Bfrom_latitude%5D=42.389131&plan%5Bfrom_longitude%5D=-71.146219&plan%5Bto%5D=Park+Street&plan%5Bto_latitude%5D=42.356395&plan%5Bto_longitude%5D=-71.062424&plan%5Btime%5D=depart&plan%5Bdate_time%5D%5Bhour%5D={hour}&plan%5Bdate_time%5D%5Bminute%5D={minute}&plan%5Bdate_time%5D%5Bam_pm%5D={AM_PM}&plan%5Bdate_time%5D%5Bmonth%5D={month}&plan%5Bdate_time%5D%5Bday%5D={day}&plan%5Bdate_time%5D%5Byear%5D={year}&plan%5Bmodes%5D%5Bsubway%5D=false&plan%5Bmodes%5D%5Bsubway%5D=true&plan%5Bmodes%5D%5Bcommuter_rail%5D=false&plan%5Bmodes%5D%5Bbus%5D=false&plan%5Bmodes%5D%5Bbus%5D=true&plan%5Bmodes%5D%5Bferry%5D=false&plan%5Boptimize_for%5D=best_route#plan_result_focus"
    elif destination == "trophy":
        # Home to Trophy Room
        url = f"https://www.mbta.com/trip-planner?plan%5Bfrom%5D=Concord+Ave+opp+Fawcett+St&plan%5Bfrom_latitude%5D=42.389131&plan%5Bfrom_longitude%5D=-71.146219&plan%5Bto%5D=Trophy+Room%2C+26+Chandler+St%2C+Boston%2C+MA%2C+02116%2C+USA&plan%5Bto_latitude%5D=42.347006&plan%5Bto_longitude%5D=-71.070533&plan%5Btime%5D=depart&plan%5Bdate_time%5D%5Bhour%5D={hour}&plan%5Bdate_time%5D%5Bminute%5D={minute}&plan%5Bdate_time%5D%5Bam_pm%5D={AM_PM}&plan%5Bdate_time%5D%5Bmonth%5D={month}&plan%5Bdate_time%5D%5Bday%5D={day}&plan%5Bdate_time%5D%5Byear%5D={year}&plan%5Bmodes%5D%5Bsubway%5D=false&plan%5Bmodes%5D%5Bsubway%5D=true&plan%5Bmodes%5D%5Bcommuter_rail%5D=false&plan%5Bmodes%5D%5Bbus%5D=false&plan%5Bmodes%5D%5Bbus%5D=true&plan%5Bmodes%5D%5Bferry%5D=false&plan%5Boptimize_for%5D=best_route#plan_result_focus"
    elif destination == "central":
        # Home to Central
        url = f"https://www.mbta.com/trip-planner?plan%5Bfrom%5D=Concord+Ave+opp+Fawcett+St&plan%5Bfrom_latitude%5D=42.389131&plan%5Bfrom_longitude%5D=-71.146219&plan%5Bto%5D=Central&plan%5Bto_latitude%5D=42.365486&plan%5Bto_longitude%5D=-71.103802&plan%5Btime%5D=depart&plan%5Bdate_time%5D%5Bhour%5D={hour}&plan%5Bdate_time%5D%5Bminute%5D={minute}&plan%5Bdate_time%5D%5Bam_pm%5D={AM_PM}&plan%5Bdate_time%5D%5Bmonth%5D={month}&plan%5Bdate_time%5D%5Bday%5D={day}&plan%5Bdate_time%5D%5Byear%5D={year}&plan%5Bmodes%5D%5Bsubway%5D=false&plan%5Bmodes%5D%5Bsubway%5D=true&plan%5Bmodes%5D%5Bcommuter_rail%5D=false&plan%5Bmodes%5D%5Bbus%5D=false&plan%5Bmodes%5D%5Bbus%5D=true&plan%5Bmodes%5D%5Bferry%5D=false&plan%5Boptimize_for%5D=best_route#plan_result_focus"
    elif destination == "work":
        # Ink Block to Work
        url = f"https://www.mbta.com/trip-planner?plan%5Bfrom%5D=300+Harrison+Avenue%2C+Boston%2C+MA%2C+02118%2C+USA&plan%5Bfrom_latitude%5D=42.346040742633&plan%5Bfrom_longitude%5D=-71.062462102185&plan%5Bto%5D=Concord+Ave+%40+Wheeler+St&plan%5Bto_latitude%5D=42.388923&plan%5Bto_longitude%5D=-71.144847&plan%5Btime%5D=depart&plan%5Bdate_time%5D%5Bhour%5D={hour}&plan%5Bdate_time%5D%5Bminute%5D={minute}&plan%5Bdate_time%5D%5Bam_pm%5D={AM_PM}&plan%5Bdate_time%5D%5Bmonth%5D={month}&plan%5Bdate_time%5D%5Bday%5D={day}&plan%5Bdate_time%5D%5Byear%5D={year}&plan%5Bmodes%5D%5Bsubway%5D=false&plan%5Bmodes%5D%5Bsubway%5D=true&plan%5Bmodes%5D%5Bcommuter_rail%5D=false&plan%5Bmodes%5D%5Bbus%5D=false&plan%5Bmodes%5D%5Bbus%5D=true&plan%5Bmodes%5D%5Bferry%5D=false&plan%5Boptimize_for%5D=best_route#plan_result_focus"
    # Send a GET request to the webpage
    headers = {"x-api-key": API_KEY}
    response = requests.get(url, headers=headers)

    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    # get only the first itinerary
    soup = soup.find(class_="m-trip-plan-results__itinerary")

    # Parse itinerary elements for display
    i_time = soup.find(class_="m-trip-plan-results__itinerary-length-time").text
    i_legs = soup.find(class_="m-trip-plan-results__itinerary-legs").text

    # split start and end times
    i_time = i_time.replace("\n", "")
    i_time = i_time.split(" - ")
    i_start = i_time[0]
    i_end = i_time[1]

    # get rid of unnecessary characters in legs
    i_legs = i_legs.replace("\n", "")

    # Print the parsed elements
    print(i_start + " - " + i_end)
    print(i_legs)

    # calculate time difference between now and start time in milliseconds
    departure = datetime.strptime(i_start, "%I:%M %p")
    departure = departure.replace(year=now.year, month=now.month, day=now.day)
    # calculate number of milliseconds that have elapsed since Unix epoch (January 1, 1970, 00:00:00 UTC)
    i_departure = int(departure.timestamp() * 1000)

    # generate a JSON update with i_time, i_legs, departure_ms, and title
    update = {
        "i_start": i_start,
        "i_end": i_end,
        "i_legs": i_legs,
        "i_departure": i_departure,
        "title": "JSON Response",
    }

    # return JSON update
    return json.dumps(update)

'''
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # parse body of POST
        body = self.rfile.read(int(self.headers["Content-Length"]))
        body = json.loads(body)
        # print body to console
        print(body)
        # call main function to get JSON update content to send as response to client
        response = main(body["route"], body["departure"])
        # send response to client
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(response), "utf-8"))
        return


with socketserver.TCPServer(("", 8000), RequestHandler) as httpd:
    print("Starting server on port 8000...")
    httpd.serve_forever()
'''