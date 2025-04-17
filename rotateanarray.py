def rotatearray(arr,n):
    length = len(arr)
    n = n % length
    return arr[n:] + arr[:n]

if __name__ == "__main__":
    arr = [1,4,6,7]
    print("Original array: ",arr)
    rotations = 3
    result = rotatearray(arr,rotations)
    print(f"Array after ",rotations,"rotations to the left: ",result)