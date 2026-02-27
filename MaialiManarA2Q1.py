"""ManarMaialiA2Q1
COMP 1012 SECTION A01
INSTRUCTOR [Saulo Q. Dos Santos]
ASSIGNMENT: A2 Question 1
AUTHOR [Manar]
VERSION [2026-Feb-26]
PURPOSE: To count how many times specified words from one file appear in another file.
"""

def InitalizeDict(wordFile: list[str]) -> dict:
    """
    Purpose:
        Initalize the dictionary with an input file, the keys are the unique words in the file, the value is 0.

    Paramters:
        wordFile: A list of strings containing the file data.

    Returns:
        Pointer to the new Dictionary with the file data.
    """
    newDict = {}
    for line in wordFile:
        line = line.strip()
        wordList = line.split(" ")
        for word in wordList:
            if word not in newDict:
                newDict[word] = 0
    return newDict


def getMaxKey(Dict: dict) -> int:
    """
    Purpose:
        Find the key with the maximum value in a dictionary.

    Paramter:
        Dict: The dictionary to go through.

    Return:
        The key with the maximum value.
    """
    max = -1
    maxKey = -1
    for key in Dict:
        if Dict[key] > max:
            max = Dict[key]
            maxKey = key
    return maxKey


def getMinKey(Dict: dict) -> int:
    """
    Purpose:
        Find the key with the minimum value in a dictionary.

    Paramter:
        Dict: The dictionary to go through.

    Returns:
        The key with the minimum value.
    """
    min = 1000000
    minKey = -1
    for key in Dict:
        if Dict[key] < min:
            min = Dict[key]
            minKey = key
    return minKey


def countWords(wordDict: dict, storyFile: list[str]) -> None:
    """
    Purpose:
        Calculate the count of each word in the story file that is in the word Dictionary.

    Paramter:
        wordDict: The dictionary containing the words. storyFile:  A list of strings containing the lines of words to look through.

    Returns:
        The key with the minimum value.
    """
    for line in storyFile:
        line = line.strip()
        wordList = line.split(" ")
        for word in wordList:
            if word in wordDict:
                wordDict[word] += 1


def printCount(wordDict: dict) -> None:
    """
    Purpose:
        Prints the word and its count.

    Paramter:
        wordDict: The dictionary to go through.

    Returns:
        None
    """
    for word in wordDict:
        print("The word '{}' appeared {} times".format(word, wordDict[word]))


def printSummary(wordDict: dict) -> None:
    """
    Purpose:
        Prints the Summary (Unique words, Maxmimu, Minmum) words and their count.

    Paramter:
        wordDict: The dictionary to go through.

    Return:
        None.
    """
    uniqueWordsSearched = len(wordDict.keys())
    print("Total unique words searched: {}".format(uniqueWordsSearched))
    maxKey = getMaxKey(wordDict)
    print('Most common word: "{}" with {} occurences'.format(maxKey, wordDict[maxKey]))
    minKey = getMinKey(wordDict)
    print('Least common word: "{}" with {} occurences'.format(minKey, wordDict[minKey]))


def printAlphabitical(wordDict: dict) -> None:
    """
    Purpose:
        Prints the words and their count in Alphabetical order.

    Paramter:
        wordDict: The dictionary to go through.

    Return:
        None.
    """
    for word in sorted(wordDict):
        print("The word '{}' appeared {} times".format(word, wordDict[word]))


def ReadFile(fileName: str) -> list[str]:
    """
    Purpose:
        Open and read the fileName.

    Paramter:
        fileName: String containing the file name to open.

    Return:
        a list of strings containing the lines of the file.
    """
    file = open(fileName, "r")
    readlines = file.readlines()
    file.close()
    return readlines


def printOutput(wordDict: dict) -> None:
    """
    Purpose:
        Prints all the details about the word dictionary.

    Parameters:
        wordDict: The dictionary to go through.

    Returns:
        None.
    """
    print("Word counts: ", end="")
    printCount(wordDict)
    print("Summary: ")
    printSummary(wordDict)
    print("Alphabetically sorted: ")
    printAlphabitical(wordDict)


# mainline
wordName = input("Enter the name of the file containing the words to search for: ")
storyName = input("Enter the name of the file containing the story to search through: ")
wordFileRead = ReadFile(wordName)
storyFileRead = ReadFile(storyName)
wordDict = InitalizeDict(wordFileRead)
countWords(wordDict, storyFileRead)
printOutput(wordDict)
print("Program terminated normally.")
