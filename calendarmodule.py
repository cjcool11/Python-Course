from datetime import date,time,datetime

DAY = date.today()
print(DAY)

now = datetime.now()
print(now)

year =  DAY.year
print(year)

month = DAY.month
print(month)

import random
#first date
day = 1
month = 1
year = 2013
#second date
day2 = 23
month2 = 12
year2 = 2024

randomday = random.randint(day,day2)
randommonth = random.randint(month,month2)
randomyear = random.randint(year,year2)
print("the random date is: ",randomday,"/",randommonth,"/",randomyear)

#hotel cost:

days = int(input("for how many days are you going to stay in the hotel for? "))

cost = 2050
result =  cost*days

print("the hotel stay would probably cost around: ",result)

#plane cost:

flighthours = int(input("for how many hours is this flight? "))

cost = 3250

result = cost*flighthours

print("your flight would probably cost around: ",result)

#rental cost:

daysrented = int(input("how many days will you rent this car? "))

cost = 560

result = cost*daysrented

print("the car rental would probably cost around: ",result)
