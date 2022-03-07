"""Reto1: Números del revés
# Descripción del reto:
# Un número del revés es un número entero que aparece igual cuando se gira 180 grados,
# por ejemplo:
# 1961 --> 1961 (Ok)
# 88 --> 88 (Ok)
# 66 --> 99 (Ko)
# 101 --> 101 (Ok)
#
# Debes crear una función capaz de sacar los números de un rango que sean reversibles.
# La función debe de recibir dos valores: Límites superior e inferior del rango (rango entre dos números (1 - 200)
# La función debe devolver los números y la cantidad de números válidos dentro de rango de los dos argumentos de entrada:
#
# Importante:
# El primer argumento siempre será menor que el segundo argumento (es decir, el
# rango siempre deberá ser válido) """


class Exercise:
    def findAllStrobogramaticNumbers(firstNumber: int, lastNumber: int):
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


print(Exercise.findAllStrobogramaticNumbers(1, 2000));
