def isEven(number: int):
    lastChar = str(number)[-1]
    if(lastChar == "0" or lastChar == "2" or lastChar == "4" or lastChar == "6" or lastChar == "8"):
        return True
    
    else:
        return False

    # MERGE CONFLICT
