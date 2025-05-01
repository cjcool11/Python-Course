def min_flips(arr):
    flips_to_0 = sum(1 for x in arr if x == '1')
    flips_to_1 = sum(1 for x in arr if x == '0')
    
    return min(flips_to_0, flips_to_1)

arr = ['1', '0', '1', '0', '1', '0']
print(min_flips(arr))