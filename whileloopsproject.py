usernum = int(input("write a number please: "))
digits = 0
temp = usernum

while temp>0:
    digits2 = temp%10
    digits += 1
    temp//=10
print("the digits inside that number are: ",digits)