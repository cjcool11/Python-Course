def find_substrings(s):
    n = len(s)
    substrings = []
    for start in range(n):
        for end in range(start, n):
            current_substring = ""
            for i in range(start, end + 1):
                current_substring += s[i]
            substrings.append(current_substring)
    return substrings

input_string = "abc"
result = find_substrings(input_string)
print("All substrings of the string:", result)
