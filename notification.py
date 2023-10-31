class Notification:
    def __init__(self, starting_location, destination, ETA, departure_time, notification_sound, route, alerts):
        self.starting_location = starting_location
        self.destination = destination
        self.ETA = ETA
        self.departure_time = departure_time
        self.notification_sound = notification_sound
        self.route = route
        self.alerts = alerts
