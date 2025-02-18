binary_input = input("Enter a binary number: ")
decimal_output = 0
length = len(binary_input)

for i in range(length):
    digit = int(binary_input[length - 1 - i])
    decimal_output += digit * (2 ** i)

print(f"The decimal equivalent of {binary_input} is {decimal_output}")
