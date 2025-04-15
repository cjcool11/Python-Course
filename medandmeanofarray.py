import array as arr

def arraymean(arr,arr_size):
    total_sum = 0
    for i in range(0, arr_size):
        total_sum += arr[i]
    return float(total_sum/arr_size)

def arraymed(arr,arr_size):
    sorted(arr)
    if arr_size % 2 != 0:
        return float(arr[int(arr_size/2)])
    return float((arr[int((arr_size-1)/2)] + arr[int(arr_size/2)])/2.0)

array = [13, 78, 98, 78, 59, 40]
array_length = len(array)
print("Array mean: ",arraymean(array,array_length))
print("Array medium: ",arraymed(array, array_length))