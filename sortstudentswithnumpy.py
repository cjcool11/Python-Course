import numpy as np

data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('Jack', 5, 48.5), ('Liam', 6, 52.5),('William', 5, 42.10), ('Mohamed', 5, 40.11)]

students = np.array(students_details,dtype = data_type)

print("orginal array: ")
print(students)
print("Array sorted bye height: ")
print(np.sort(students, order = "height"))