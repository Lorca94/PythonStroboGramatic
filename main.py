def findallstrobogramaticnumbers(firstNumber: int, lastNumber: int):
    if firstNumber >= lastNumber:
        return "Error: The first number entered must always have a value less than the second number entered"
    else:
        listStrobo = []
        b = 0
        for x in range(firstNumber, lastNumber + 1):
            if x > 10:
                listProve = []
                xDigit = [int(a) for a in str(x)]
                for i in xDigit:
                    if i == 6 or i == 9:
                        if i == 6:
                            listProve.append(9)
                        else:
                            listProve.append(6)
                    else:
                        listProve.append(i);
                listProve.reverse()
                if listProve == xDigit:
                    listStrobo.append(x)
        return listStrobo


print(findallstrobogramaticnumbers(1, 2000));
