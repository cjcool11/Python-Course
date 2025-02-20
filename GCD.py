smallest_num = int(input("enter the smallest number: "))
largest_num = int(input("enter the largest number: "))

while(smallest_num):
    numberstore = smallest_num
    smallest_num = largest_num % smallest_num
    largest_num = numberstore

print("GCD is: ",largest_num)