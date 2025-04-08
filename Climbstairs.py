def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    twoStair = 0
    oneStair  = 0
    if(stairs>=2):
        twoStair=ways(stairs-2)
    oneStair = ways(stairs-1)
    return twoStair + oneStair

Stairs = int(input("Enter the number of stairs: "))
print("The amount of ways to climb the stairs: ",ways(Stairs))