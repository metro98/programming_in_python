def planet(id):
    planets = {
        1 : "Mercury",
        2 : "Venus",
        3 : "Earth",
        4 : "Mars",
        5 : "Jupiter",
        6 : "Saturn",
        7 : "Uranus",
        8 : "Neptune",
        9 : "Pluto"
    }

    return planets[id]

play = True
while play:
    number = int(input("Enter the id of the planet: "))
    print(planet(number))
    next = input("Do you wanna try next one: ")
    if next == "no":
        play = False
    else:
        continue

