class RouteHandler:
    def __init__(self):
        self.state = "Wait for Destination Input"
        self.destination = None
        self.eta = None
        self.optimal_route = None

    def run(self):
        while True:
            if self.state == "Wait for Destination Input":
                self.destination = input("Enter destination: ")
                self.state = "Query Real-Time ETA Routine"

            elif self.state == "Query Real-Time ETA Routine":
                self.eta = query_eta(self.destination)
                self.state = "Wait for Solve"

            elif self.state == "Wait for Solve":
                if is_eta_ready():
                    self.state = "Receive Optimal Route"

            elif self.state == "Receive Optimal Route":
                self.optimal_route = receive_optimal_route()
                self.state = "Send Route Info to Human Interfaces"

            elif self.state == "Send Route Info to Human Interfaces":
                send_route_info(self.eta, self.optimal_route)
                self.state = "Wait for Destination Input"

def query_eta(destination):
    # code to query real-time ETA information for the selected destination
    pass

def is_eta_ready():
    # code to check if ETA information is ready
    pass

def receive_optimal_route():
    # code to receive the optimal route information calculated based on real-time ETA data
    pass

def send_route_info(eta, optimal_route):
    # code to send the route information, including ETA and the optimal route, to the user interfaces where it can be displayed to the user
    pass
