def honai(n, a, b, c):
    if n == 1:
        print("Move disk 1 from rod ",a,"To rod ",b)
        return
    honai(n-1,a,c,b)
    print("Move disk ",n,"From rod ",a,"To rod ",b)
    honai(n-1,c,b,a)

n = 9
honai(n, "A", "C" , "B")