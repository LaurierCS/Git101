"""
    Checks if the given number is even
    @param number: The number to check
    @return: True if the number is even, False if not
"""
def isEven(number: int):
    lastChar = str(number)[-1]
    if(lastChar == "0" or lastChar == "2" or lastChar == "4" or lastChar == "6" or lastChar == "8"):
        return True

    else:
        return False

"""
    Checks if the given number is odd
    @param number: The number to check
    @return: True if the number is odd, False if not
"""
def isOdd(number: int):
    return not isEven(number);
