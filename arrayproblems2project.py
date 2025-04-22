def max_difference(arr):
    if not arr or len(arr) < 2:
        return None
    
    min_element = arr[0]
    max_diff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element
        if arr[i] < min_element:
            min_element = arr[i]

    return max_diff

arr = [7, 1, 5, 3, 6, 4]
print("Maximum difference:", max_difference(arr))