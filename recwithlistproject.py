def calculate_length_recursive(lst):
    if not lst:
        return 0
    return 1 + calculate_length_recursive(lst[1:])

sample_list = [1, 2,234,234,745,3,6,653]
length = calculate_length_recursive(sample_list)
print(f"The length of the list is: {length}")