import azure.functions as func
import logging
from direct import eta

app = func.FunctionApp()
@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)

def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # check if method is GET
    if req.method == "GET":
        # get the data from the query string
        route = req.params.get("route")
        departure = req.params.get("departure")

        # call eta function to get JSON update content to send as response to client
        response = eta(route, departure)

        # send response to client
        return func.HttpResponse(response, status_code=200)