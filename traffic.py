# Name: Swapnil Srivastava

# traffic.py

# Problem: This program calculates
#               the average number of vehicles traveling on each road
#               and average number of vehicles traveling per road

# Certification of Authenticity:

# I certify that this lab is entirely my own work.

def averageVehicles():

    # Get input of number of roads
    numRoads = eval(input("Enter the number of roads here: "))
    # define variable for road number
    displayNum = 0
    # define variable to calculate total number of vehicles
    totalVehicles = 0
    # Create loop using number of roads to calculate for each road
    for i in range(numRoads):
        displayNum = displayNum + 1
        # Define variable for day number
        day = 0
        # Define variable for total vehicles for the perticular road
        sumVehicle = 0
        print("For road", displayNum, ":")
        # Get input for total days surveyed for perticular road
        numDays = eval(input("Number of days road surveyed: "))
        # Create loop to get vehicle amount for each day
        for j in range(numDays):
            day = day + 1
            print("For day", day, ":")
            numVehicles = eval(input("number of vehicles on day: "))
            print()
        # Calculate total vehicles for this road
            sumVehicle = sumVehicle + numVehicles
        # Calculate average of vehicles per day for this perticulas road
        average = sumVehicle/numDays
        # Display output on user monitor
        outputAvgVehicle = str("The average of vehicles for road")
        print(outputAvgVehicle, displayNum, "is:", average)
        print()
        # Calculate total vehicles for all roads
        totalVehicles = sumVehicle + totalVehicles
    # Display output for total number of roads
    outputTotal = str("Total number of vehicles traveled on all roads: ")
    print(outputTotal, totalVehicles)
    print()
    # Calculate average of vehicles per road
    averagePerRoad = totalVehicles/numRoads
    # Display output for average per road
    print("Average number of vehicles per road is:", averagePerRoad)
