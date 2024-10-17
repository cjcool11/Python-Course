import os

input = input("do you want to shutdown your machine? ")

if input == "no":
    exit()
else:
    os.system("shutdown /s /t 1")