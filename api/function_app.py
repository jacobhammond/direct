import azure.functions as func
import logging
from direct import *

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function(name="http_trigger")

@app.route(route="http_trigger", auth_level=func.AuthLevel.FUNCTION)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:

    # Read request headers
    logging.info(req.headers)

    # parse body of POST
    body = req.get_json()

    # Print body to console
    logging.info(body)

    # call eta function to get JSON update content to send as response to client
    response = eta(body["route"], body["departure"])

    # send response to client
    return func.HttpResponse(
        body=json.dumps(response),
        mimetype="application/json",
        status_code=200
    )