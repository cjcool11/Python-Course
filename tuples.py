tuple1 = ("qwerty",12,"hi")
tuple2 = (42,35,64,35)
tuple3 = tuple1 + tuple2 + (9,)
print(tuple3)
is35intuple = tuple3.count(35)
print(is35intuple)

slice = tuple2[1:3]
print(slice)


tupole5 = (1,2,3,3,2,1)
tupolerev = tupole5[::-1]
if tupole5 == tupolerev:
    print("the tupleis the same when reversed!!!")
else:
    print("the tuple is not the same when reversed!!!")

weather = (1,0,0,0,1,1,0)
sunny = weather.count(0)
rainy = weather.count(1)
if sunny > rainy:
    print("it will be sunny!!!")
else:
    print("it is going to be rainy:(")