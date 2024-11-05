#activity 3
fruits = ["apple", "banana", "cherry", "date"]

print("Original list:", fruits)

fruits.append("elderberry") 
print("After appending an element:", fruits)

fruits.remove("banana") 
print("After removing an element by value:", fruits)

length = len(fruits) 
print("Length of the list:",length)

#actual project

start_range = int(input("Enter the start of the range: "))

end_range = int(input("Enter the end of the range: ")) 

squares = [x**2 for x in range(start_range, end_range + 1)] 
odd_squares = [num for num in squares if num % 2 != 0] 
even_squares = [num for num in squares if num % 2 == 0] 

print("Squares:", squares) 
print("Odd Squares:", odd_squares) 
print("Even Squares:", even_squares)

