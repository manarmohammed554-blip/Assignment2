"""ManarMaialiA2Q3
COMP 1012 SECTION A01
INSTRUCTOR [Saulo Q. Dos Santos]
ASSIGNMENT: A2 Question 3
AUTHOR [Manar]
VERSION [2026-Feb-26]
PURPOSE: To read bitcoin price data from a file,
         and calculate the statistics.
"""

import math


def readBitcoinData() -> list[tuple]:
    """
    Purpose:
        Read the input file, fill a list with the data needed in tuples.

    Paramters:
        None

    Returns:
        Pointer to the new list with the file data.
    """
    outputList = []
    bitcoinFileName = input("Enter bitcoin file name: ")
    bitcoinFile = open(bitcoinFileName, "r")
    # Skip the header file
    bitcoinFile.readline()
    # Read the data
    for line in bitcoinFile:
        data = line.strip().split(",")
        dataTuple = (data[0], float(data[1]))
        outputList.append(dataTuple)
    bitcoinFile.close()
    return outputList


def calcSum(Data: list) -> int:
    """
    Purpose:
        Calculate the sum of the prices in the list of Data.

    Paramters:
        Data: a list of tuples containing bitcoin info.

    Returns:
        The sum of the prices in the list.
    """
    sum = 0
    for item in Data:
        sum = sum + item[1]
    return sum


def calcMean(Data: list[tuple]) -> float:
    """
    Purpose:
        Calculate the mean of the prices in the list of Data.

    Paramters:
        Data: a list of tuples containing bitcoin info.

    Returns:
        The mean of the prices in the list.
    """
    sum = calcSum(Data)
    mean = sum / len(Data)
    return mean


def calcStandardDeviation(Data: list) -> float:
    """
    Purpose:
        Calculate the standard deviation of the prices in the list of Data.

    Paramters:
        Data: a list of tuples containing bitcoin info.

    Returns:
        The standard deviation of the prices in the list.
    """
    mean = calcMean(Data)
    differenceSum = 0
    for item in Data:
        tempValue = (item[1] - mean) ** 2
        differenceSum += tempValue
    stdDeviation = math.sqrt(differenceSum / len(Data))
    return stdDeviation


def getMaxValue(Data: list) -> int:
    """
    Purpose:
        Calculate the max of the prices in the list of Data.

    Paramters:
        Data: a list of tuples containing bitcoin info.

    Returns:
        The index of the max value in the list.
    """
    index = 0
    maxIndex = 0
    maxValue = Data[0][1]
    for item in Data:
        if item[1] > maxValue:
            maxValue = item[1]
            maxIndex = index
        index += 1
    return maxIndex


def getMinValue(Data: list) -> int:
    """
    Purpose:
        Calculate the minimum of the prices in the list of Data.

    Paramters:
        Data: a list of tuples containing bitcoin info.

    Returns:
        The index of the minimum value in the list.
    """
    index = 0
    minIndex = 0
    minValue = Data[0][1]
    for item in Data:
        if item[1] < minValue:
            minValue = item[1]
            minIndex = index
        index += 1
    return minIndex


def getPriceIncreaseStats(Data: list) -> tuple:
    """
    Purpose:
        Calculate the increasing change in the data, with the maximum difference.

    Paramters:
        Data: a list of tuples containing bitcoin info.

    Returns:
        A tuple containing:
        maxDiff: integer representing the max difference in price in subsequent days.
        maxIndex: the index representing the index of the maximum price in the list.
        numOfDays: integer representing the number of days with an increase in price.
    """
    numOfDays = 0
    maxIndex = 0
    maxDiff = -1

    for index in range(1, len(Data)):
        tempVal = Data[index][1] - Data[index - 1][1]
        if tempVal > 0:
            numOfDays += 1
            if tempVal > maxDiff:
                maxDiff = tempVal
                maxIndex = index
    outputTuple = (maxDiff, maxIndex, numOfDays)
    return outputTuple


def getPriceDecreaseStats(Data: list) -> tuple:
    """
    Purpose:
        Calculate the decreasing change in the data, with the minimum difference.

    Paramters:
        Data: a list of tuples containing bitcoin info.

    Returns:
        A tuple containing:
        minDiff: integer representing the min difference in price in subsequent days.
        minIndex: the index representing the index of the minimum price in the list.
        numOfDays: integer representing the number of days with a decrease in price.
    """
    numOfDays = 0
    minIndex = 0
    minDiff = 1000000000000

    for index in range(1, len(Data)):
        tempVal = Data[index][1] - Data[index - 1][1]
        if tempVal < 0:
            numOfDays += 1
            if tempVal < minDiff:
                minDiff = tempVal
                minIndex = index
    outputTuple = (minDiff, minIndex, numOfDays)
    return outputTuple


def printPriceChange(Data: list) -> None:
    """
    Purpose:
        Print the price change in the data.

    Paramters:
        Data: a list of tuples containing bitcoin info.

    Returns:
        None
    """
    print("Price Movement Analysis:")
    increaseTuple = getPriceIncreaseStats(Data)
    decreaseTuple = getPriceDecreaseStats(Data)
    print("Days with a price increase: {}".format(increaseTuple[2]))
    print("Days with a price decrease: {}".format(decreaseTuple[2]))
    print(
        "Largest single-day increase: ${:,.2f} on {}".format(
            increaseTuple[0], Data[increaseTuple[1]][0]
        )
    )
    print(
        "Largest single-day decrease: ${:,.2f} on {}".format(
            abs(decreaseTuple[0]), Data[decreaseTuple[1]][0]
        )
    )


def printPriceStats(Data: list) -> None:
    """
    Purpose:
        Print the statistics(Mean, Minimum, Maximu, Standard deivation) in the data.

    Paramters:
        Data: a list of tuples containing bitcoin info.

    Returns:
        None
    """
    print("Price statistics:")
    print("Average Price: ${:,.2f}".format(calcMean(Data)))
    minIndex = getMinValue(Data)
    print("Minimum Price: ${:,.2f} on {}".format(Data[minIndex][1], Data[minIndex][0]))
    maxIndex = getMaxValue(Data)
    print("Minimum Price: ${:,.2f} on {}".format(Data[maxIndex][1], Data[maxIndex][0]))
    print("Standard Deviation: ${:,.2f}".format(calcStandardDeviation(Data)))


def printAnalysis(Data: list) -> None:
    """
    Purpose:
        Print the statistics and price change in the data.

    Paramters:
        Data: a list of tuples containing bitcoin info.

    Returns:
        None
    """
    print("Bitcon Price Statistics")
    print("========================")
    printPriceStats(Data)
    printPriceChange(Data)
    print("Program terminated normally.")


# mainline
bitcoinData = readBitcoinData()
printAnalysis(bitcoinData)
