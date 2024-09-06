Temperature = int(input("Write the temperature in your city in celsius: "))
if Temperature < 32:
    print("it is cold now, please wear a jacket")
elif Temperature == 32:
    print("the weather is perfect today")
else:
    print("it is hot today, please wear a light clothes")