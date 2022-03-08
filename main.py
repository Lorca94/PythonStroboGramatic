def findallstrobogramaticnumbers(firstNumber: int, lastNumber: int):
    if firstNumber >= lastNumber:
        return "Error: The first number entered must always have a value less than the second number entered"
    else:
        listStrobo = []
        b = 0
        for actualNumber in range(firstNumber, lastNumber + 1):
            if actualNumber > 10:
                reverseDigit = []
                actualnumberdigit = [int(a) for a in str(actualNumber)]
                for i in actualnumberdigit:
                    if i == 6 or i == 9:
                        if i == 6:
                            reverseDigit.append(9)
                        else:
                            reverseDigit.append(6)
                    else:
                        reverseDigit.append(i);
                reverseDigit.reverse()
                if reverseDigit == actualnumberdigit:
                    actualnumberrev = ''.join(map(str, reverseDigit))
                    listStrobo.append(actualnumberrev)
        return listStrobo, len(listStrobo)


print(findallstrobogramaticnumbers(1, 2000));
