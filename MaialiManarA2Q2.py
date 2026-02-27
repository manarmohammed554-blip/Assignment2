"""ManarMaialiA2Q2
COMP 1012 SECTION A01
INSTRUCTOR [Saulo Q. Dos Santos]
ASSIGNMENT: A2 Question 2
AUTHOR [Manar]
VERSION [2026-Feb-26]
PURPOSE: To read parkade occupancy data from a file,
         and calculate the occupancy rate for each floor, 
         and determine the parking rate based on the occupancy levels.
"""

"""
The data structure used is a list of tuples, because the data is related but not the same, thus a tuple is suitable
and a list to store multiple tuples holding multiple data for each floor/line in the file
"""

import math


def InitalizeData() -> tuple[list[tuple], int, int]:
    """
    Purpose:
        Read the input file, fill a list with the data needed in tuples.

    Paramters:
        None

    Returns:
        Pointer to the new list with the file data.
    """
    fileName = input("Enter the name of the file: ")
    file = open(fileName, "r")

    newList = []

    for line in file:
        inputData = line.strip().split(",")
        # turn the input data into integers for the calculations
        inputData = [int(x) for x in inputData]
        # Create new tuple with the input data
        newTuple = tuple(inputData)
        newList.append(newTuple)

    file.close()
    return newList


def choosePrice(occupancyRate: int) -> float:
    """
    Purpose:
        Choose the price of the floor based on occupancy rate.

    Paramters:
        occupancyRate: integer representing the floor occupancy rate.

    Returns:
        An integer representing the price of the floor.
    """
    if occupancyRate >= 75:
        return 3.0
    elif occupancyRate < 75 and occupancyRate >= 60:
        return 2.0
    elif occupancyRate < 60 and occupancyRate >= 50:
        return 1.50
    elif occupancyRate < 50 and occupancyRate >= 0:
        return 1.0


def getSpace(parkadeList: list[tuple]) -> tuple[int, int]:
    """
    Purpose:
        Calculate the maximum space and occupied space in the parkade.

    Paramters:
        parkadeList: the list containing all parkade information

    Returns:
        a tuple of integers containing the total space and the occupied space
    """
    totalMaxSpace=0
    totalOccupiedSpace=0
    
    for floor in parkadeList:
        totalMaxSpace += floor[1]
        totalOccupiedSpace += floor[2]
    return totalMaxSpace, totalOccupiedSpace


def printFullParkade() -> None:
    """
    Purpose:
        Print info that the parkade is full.

    Paramters:
        None

    Returns:
        None.
    """
    print("PARKADE FULL\n")
    print("----------")


def printParkadeSummary(maxSpace: int, occupiedSpace: int) -> None:
    """
    Purpose:
        Print the total occupied space, available space and occupancy rate of the parkade.

    Paramters:
        maxSpace: integer representing the maximum space in the parkade.
        occupiedSpace: integer representing the occupied space in the parkade.

    Returns:
        None.
    """
    print("Total space in parkade: {}".format(maxSpace))
    print("Total availale spaces: {}".format(maxSpace - occupiedSpace))
    parkadeOccupancyRate = (occupiedSpace / maxSpace) * 100
    print(
        "Total parkade occupancy rate: {:.0f}%".format(math.floor(parkadeOccupancyRate))
    )


def printFloorInfo(parkadeList: list[tuple]) -> None:
    """
    Purpose:
        Print information about the floors in the parkade.

    Paramters:
        parkadeList: a list containing all info about the parkade.

    Returns:
        None.
    """
    for floor in parkadeList:
        availableSpaces = floor[1] - floor[2]
        occupancyRate = (floor[2] / floor[1]) * 100
        if availableSpaces > 0:
            print(
                "Floor: {} {} available spaces, {:.0f}% occupancy, parking rate is ${:.2f}".format(
                    floor[0], availableSpaces, occupancyRate, choosePrice(occupancyRate)
                )
            )
        else:
            print("Floor: {} FLOOR FULL".format(floor[0]))
    print("----------")


# mainline
parkadeList = InitalizeData()
maxSpace, occupiedSpace = getSpace(parkadeList)
if maxSpace == occupiedSpace:
    printFullParkade()
else:
    printFloorInfo(parkadeList)
printParkadeSummary(maxSpace, occupiedSpace)
print("\nProgram terminated normally.")
