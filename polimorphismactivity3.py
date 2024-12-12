from abc import ABC, abstractmethod

class countries(ABC):
    def countryinfo(self):
        pass

class Emirates(countries):
    def countryinfo(self):
        print("Emirates: I am a desert!")
        print("Emirates: I have the currency of AED/Dirham!")
        print("Emirates: I am located in the middle east!")

class USA(countries):
    def countryinfo(self):
        print("USA: I am a forest!")
        print("USA: I have the currency of $/Dollars!")
        print("USA: I am located at north america!")

Emiratescountry = Emirates()
countryUSA = USA()

for country in (Emiratescountry,countryUSA):
    country.countryinfo()

