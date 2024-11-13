number_of_countries = int(input("How many countries you want to enter: "))


countries = {}

for i in range(number_of_countries):
    name = input("Enter the countries name: ")
    if name[0].upper() not in countries:
        countries[name[0].upper()] =  [ name ]
    else:
        countries[name[0].upper()].append(name)

print(countries)