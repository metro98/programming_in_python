birthdays = {
    "Sachin" : "03/14/2003",
    "Carl" : "01/17/2001",
    "Khan" : "06/14/2010",
    "Rohan" : "01/6/2005"
}

name = input("Enter you name")

if name in birthdays:
        print(birthdays[name])
else:
        print("Name not found")