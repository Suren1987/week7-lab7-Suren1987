# Name: Surendra Shrestha
# Assignment title: Refugee Stats with Dictionaries.
# Time to complete: 30 minutes.
# Description: This script contains three functions that derives three different outputs using the refugee 
# data obtained from https://en.wikipedia.org/wiki/Refugee_camp. First, I created a dictionary 
# with 5 key-value pairs consisting of a country name and an integer that represents the number of refugees
# in refugee camps in five different countries, for year 2014. The first function prints out just the 
# countries' name. The second function prints out just the population. The third function prints out a series
# of statements stating the number of refugees for each country.

Refugee_Country = {'Algeria': 90000, 'Botswana': 2833, 'Djibouti': 18208, 'India': 65057, 'Mauritania': 48910}

# Print selected countries only
def printCountry(Refugee_Country):
    for key in Refugee_Country.keys():
        print key
printCountry(Refugee_Country)

# Print the number of refugees only for the selected countries
def printNumber(Refugee_Country):
    for value in Refugee_Country.values():
        print value
printNumber(Refugee_Country)

# Print selected countries with their number of refugees for year 2014
def printCountryRefugee(Refugee_Country):
    for (key, value) in Refugee_Country.items():
        print key, "has", value, "refugees."
printCountryRefugee(Refugee_Country)
