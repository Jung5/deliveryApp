# WGU #011047348
# Jeongwook Na
# C950 Task 2

# was imported to change status of Package 9 at given time.
import datetime


class Packages:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes, status, departureTime, deliveryTime):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.departureTime = None
        self.deliveryTime = None

    def __str__(self):
        return "id: %s, Address: %s, City: %s, State: %s, ZipCode: %s, Deadline: %s, Weight: %s, Note: %s, Departure Time: %s, Delivery Time: %s" % (
        self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.status,
        self.departureTime, self.deliveryTime)

    # This method sets status of packages at a given time.
    def setStatus(self, inputTime):
        if inputTime >= self.deliveryTime:
            self.status = "Delivered"
        elif inputTime >= self.departureTime:
            self.status = "En Route"
        else:
            self.status = "At the Hub"
        # will find Package #9 and corrects address after 10:20 am
        if self.id == 9:
            if inputTime >= datetime.timedelta(hours=10, minutes=20):
                self.address = "410 S State St"
                self.zip = "84111"
            # needs else to revert back to original address in case of multiple search.
            else:
                self.address = "300 State St"
                self.zip = "84103"