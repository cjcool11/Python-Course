items = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency_dict = {}

for item in items:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1

print(frequency_dict)