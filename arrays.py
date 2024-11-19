import array as arr

array1 = arr.array("i",[1, 3, 5, 3, 7, 9, 3])
print("this is the original array: "+str(array1))
count3 = array1.count(3)
print("this is the number of occurences with the number 3: ",count3)
array1.reverse()
print("this is the array in reverse: ",str(array1))

