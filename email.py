email = input("Enter you email address: ")

user_list = email.split("@")
#print(user_list)

user_name = user_list[0]
domain = user_list[1]
print (user_name)
print(domain)
