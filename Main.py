# WGU #011047348
# Jeongwook Na
# C950 Task 2

import csv
import datetime
from HashTable import HashTable
from Packages import Packages
from Trucks import Trucks

# Loading three CSV files: Address, Distance, and Package.
with open("CSV/Address.csv") as addressCSV:
    AddressCSV = csv.reader(addressCSV)
    AddressCSV = list(AddressCSV)
with open("CSV/Distance.csv") as distanceCSV:
    DistanceCSV = csv.reader(distanceCSV)
    DistanceCSV = list(DistanceCSV)
with open("CSV/Package.csv") as packageCSV:
    PackageCSV = csv.reader(packageCSV)
    PackageCSV = list(PackageCSV)

# This code bases off of C950 - Webinar-2 - Getting Greedy, who moved my data?
# This loads the data from package csv file, and uses its data to create a hash table containing package objects.
def loadPackage(filename):
    with open(filename) as packageCSV:
        pData = csv.reader(packageCSV, delimiter=',')
        next(pData)
        for package in pData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pNotes = package[7]
            pStatus = "At the Hub"
            pDepartureTime = None
            pDeliveryTime = None

            # creating package object
            p = Packages(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pNotes, pStatus, pDepartureTime,
                         pDeliveryTime)
            # Inserts data into pHash
            pHash.insert(pID, p)

# Creates pHash - hash table.
pHash = HashTable()

# This code bases off of C950 WGUPS Project Implementation Steps - Example
# finds the address ids, which are necessary to calculate distances between two locations.
def getAddressID(address):
    for row in AddressCSV:
        if address in row[2]:
            return int(row[0])

# This code bases off of C950 WGUPS Project Implementation Steps - Example
# finds the distance between two locations base on distance csv file.
def getDistance(x, y):
    distanceCoordinate = DistanceCSV[x][y]
    if distanceCoordinate == '':
        distanceCoordinate = DistanceCSV[y][x]
    return float(distanceCoordinate)

# loads data from csv file into hash table.
loadPackage('CSV/Package.csv')

# Packages with the same delivery address are mostly grouped together.
# Package #5 and #9 needs to paired together.
# Packages 13, 14, 15, 16, 19, 20 has to be delivered together
# Earliest departure time 8 am => Truck 1,
# Packages with specific deadline were not put in Truck 2.
# Packages 3, 18, 36, 38 has to be delivered via Truck 2
# Because of Package #9 gets updated at 10:20 am, Truck 2 departs at 10:20.
# Packages 6, 25 needs to be delivered until 10:30. arrives at the depot at 9:05. => Truck 3.
# Delayed Packages to Truck 3. Other packages distributed among three trucks.

## Create truck objects to manually load them.
## Departs from the hub at the given times.
truck1 = Trucks("4001 South 700 East", [1,7,10,13,14,15,16,19,20,21,29,30,35,37], 0.0, datetime.timedelta(hours=8))
truck2 = Trucks("4001 South 700 East", [3,4,8,11,17,18,22,23,24,33,36,38], 0.0,  datetime.timedelta(hours=10, minutes=20))
truck3 = Trucks("4001 South 700 East", [2,5,6,9,12,25,26,27,28,31,32,34,39,40], 0.0, datetime.timedelta(hours=9, minutes=5))

# This method uses the nearest neighbor algorithm.
def deliverySimulation(truck):
    # creates an empty list to add the packages that need to be delivered.
    packagesLeft = []
    # adds (=append) packages(id) that need to be delivered to packagesLeft.
    for pID in truck.packages:
        package = pHash.search(pID)
        packagesLeft.append(package)
    # this is necessary to prior to adding packages in order following my algorithm.
    truck.packages.clear()

    # the algorithm runs until there is no more packages left to be delivered.
    # will add the closest packages in order.
    while len(packagesLeft) > 0:
        nextAddress = 2000
        nextDelivery = None
        # assigns next package to be delivered to a package that is closest to the truck's location.
        for package in packagesLeft:
            if getDistance(getAddressID(truck.address), getAddressID(package.address)) <= nextAddress:
                nextAddress = getDistance(getAddressID(truck.address), getAddressID(package.address))
                nextDelivery = package

        # adds closest package from the truck into the cleared truck.
        truck.packages.append(nextDelivery.id)
        # removes the package that has been added to the truck from the delivery list.
        packagesLeft.remove(nextDelivery)
        # sums up total mileage to calculate total mileage later on in the program.
        truck.totalMiles += nextAddress
        # moves the truck to next location
        truck.address = nextDelivery.address
        # updates how long the truck has taken to get to the current location.
        # speed of the truck is always 18 mph.
        truck.tempTime += datetime.timedelta(hours=nextAddress / 18)
        # sets next package to be delivered to calculate the distance for next delivery.
        nextDelivery.deliveryTime = truck.tempTime
        nextDelivery.departureTime = truck.departureTime



# There are three trucks with two drivers. Also, trucks instantaneously load packages.
deliverySimulation(truck1)
deliverySimulation(truck3)
# Truck 2 will leave after either one of two drivers return first by using min (chooses lower value of the two).
truck2.departureTime = min(truck1.tempTime, truck3.tempTime)
deliverySimulation(truck2)


#UI for users
print("C950 Project by Jeongwook Na // WGU #011047348")
print("                Menu Options:")
print("**********************************************")
print("1. Print All Package Status and Total Mileage")
print("2. Get a Single Package Status with a Time")
print("3. Exit the Program")
print("**********************************************")

ans = int(input())

while True:
    if ans == 1:
        cont = input("Continue? (y/n): ")
        if cont == "y":
            inputTime = input("Enter a time in the format of HH:MM: ")
            print("Total Mileage:", (truck1.totalMiles + truck2.totalMiles + truck3.totalMiles))
            (h, m) = inputTime.split(":")
            timeInput = datetime.timedelta(hours=int(h), minutes=int(m))
            printAll = range(1, 41)
            for pID in printAll:
                package = pHash.search(pID)
                package.setStatus(timeInput)
                print(str(package))
        else:
            print("Exiting the program...")
            break
    elif ans == 2:
        cont = input("Continue? (y/n): ")
        if cont == "y":
            inputTime = input("Enter a time in the format of HH:MM: ")
            (h, m) = inputTime.split(":")
            timeInput = datetime.timedelta(hours=int(h), minutes=int(m))
            inputID = [int(input("Enter the package id(number): "))]
            for pID in inputID:
                package = pHash.search(pID)
                package.setStatus(timeInput)
                print(str(package))
        else:
            print("Exiting the program...")
            break
    else:
        print("Exiting the program...")
        break