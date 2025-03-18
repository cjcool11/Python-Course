def divide(ousdividend, ourdivisor):
    sign = -1 if ((ousdividend < 0) ^ (ourdivisor < 0)) else 1
    ousdividend = abs(ousdividend)
    ourdivisor = abs(ourdivisor)
    quotientnumber = 0
    tempnumber = 0
    for i in range(31, -1, -1):
        if (tempnumber + (ourdivisor << i) <= ousdividend):
            tempnumber += ourdivisor << i
            quotientnumber |= 1 << i
    if sign == -1:
        quotientnumber = -quotientnumber
    return quotientnumber

a = int(input("Enter your dividend: "))
b = int(input("Enter your divisor: "))
print("a / b = ", divide(a, b))
