def get_location(city, country):
    location = city + ', ' + country
    return location

stad = input("In what city do you live? ")
land = input("In what country do you live? ")

locatie = get_location(stad,land)
print(locatie)

