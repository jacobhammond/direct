import azure.functions as func
import logging
from  direct import *

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
@app.route(route="req")

def main(req: func.HttpRequest) -> func.HttpResponse:

    # check if method is GET
    if req.method == "GET":
        # get the data from the query string
        route = req.params.get("route")
        departure = req.params.get("departure")

    # call eta function to get JSON update content to send as response to client
    response = eta(route, departure)

    # send response to client
    return func.HttpResponse(bytes(json.dumps(response), "utf-8"), status_code=200)