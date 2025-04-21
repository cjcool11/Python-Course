def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

n = 5
arr = [1, 2, 3, 5]
missing = find_missing_number(arr, n)
print("Missing number:", missing)