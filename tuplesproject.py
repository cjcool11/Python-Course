#Teacher, you can modify the three numbers in the tuple but please do not add more numbers!But i dont kn ow if you can modify through github!!!
tuple1 = (23,12,8)
tuple1len = len(tuple1)
for i in range(tuple1len):
    result = tuple1[0] * tuple1[1]
    result = result * tuple1[2]
print(result)


