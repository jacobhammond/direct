import azure.functions as func
import logging
from direct import *

##app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
#@app.function(name="http_trigger")
#@app.route(route="http_trigger")

def http_trigger(req: func.HttpRequest) -> func.HttpResponse:

    # Read request headers
    logging.info(req.headers)

    # parse body of POST
    body = json.loads(req.get_body())

    # Print body to console
    logging.info(body)

    # call eta function to get JSON update content to send as response to client
    response = eta(body["route"], body["departure"])

    # send response to client
    return func.HttpResponse(
        bytes(json.dumps(response), "utf-8"),
        mimetype="application/json",
        status_code=200
    )