def longest_alternating_subarray(arr):
    if not arr:
        return 0

    max_length = 1
    curr_length = 1

    for i in range(1, len(arr)):
        if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
            curr_length += 1
            max_length = max(max_length, curr_length)
        else:
            curr_length = 1

    return max_length

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(longest_alternating_subarray(arr))