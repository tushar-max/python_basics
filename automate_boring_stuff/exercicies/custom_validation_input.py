import pyinputplus as pyip

def addsUpToTen(numbers):
    """
    Say you want the user to enter a series of digits that adds up to 10.
    """
    numbersList = list(numbers)

    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)

        if sum(numbersList) != 10:
            raise Exception("The digits must add up to 10, not %s." % (sum(numbersList)))

    return int(numbers)



response = pyip.inputCustom(addsUpToTen)
