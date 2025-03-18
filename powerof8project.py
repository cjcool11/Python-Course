def is_power_of_8(n):
    if n <= 0:
        return False
    if (n & (n - 1)) != 0:
        return False
    position = 0
    while n > 1:
        n >>= 1
        position += 1
    return position % 3 == 0

number = int(input("Enter a number: "))
if is_power_of_8(number):
    print(f"{number} is a power of 8.")
else:
    print(f"{number} is not a power of 8.")
