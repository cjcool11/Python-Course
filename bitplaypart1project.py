def rightmost_set_bit(n):
    return n & -n

number = 10
result = rightmost_set_bit(number)
print(f"The rightmost set bit in {number} is {result}")
