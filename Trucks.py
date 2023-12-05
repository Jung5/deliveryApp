# WGU #011047348
# Jeongwook Na
# C950 Task 2

class Trucks:
    def __init__(self, address, packages, totalMiles, departureTime):
        self.address = address
        self.totalMiles = totalMiles
        self.packages = packages
        self.tempTime = departureTime
        self.departureTime = departureTime

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (
        self.address, self.totalMiles, self.packages, self.tempTime, self.departureTime)

