def romantoint(inputroman):

    romans = {"M" : 1000, "D" : 500, "C" : 100, "L" :50, "X" : 10, "V" : 5, "I" :1}

    resultinteger = 0

    for i in range(0, len(inputroman) -1):
        if romans[inputroman[i]] < romans[inputroman[i+1]]:
            resultinteger -= romans[inputroman[i]]
        else:
            resultinteger += romans[inputroman[i]]
    return resultinteger + romans[inputroman[-1]]

roman = input("enter roman numeral: ")

print("integer equivelant: ",romantoint(roman))