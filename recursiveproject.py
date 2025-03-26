#function 1
counter = 0

def fac_with_counter(n):
    global counter
    counter += 1
    if n == 1 or n == 0:
        return 1
    return n * fac_with_counter(n - 1)

n = 5
counter = 0
result = fac_with_counter(n)
print(f"Factorial of {n} is {result}")
print(f"Number of iterations: {counter}")

#function 2

counter = 0

def onetoten_with_counter(n):
    global counter
    counter += 1
    if n > 10:
        return
    print(n)
    onetoten_with_counter(n + 1)

counter = 0
onetoten_with_counter(1)
print(f"Number of iterations: {counter}")