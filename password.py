#Enter first password
first_password = input("Enter the password: ")

#Enter the second password
confirm_password = input("Enter the password to confirm: ")

if first_password == confirm_password:
    print("Your password is set")
elif first_password.lower() == confirm_password.lower():
        print("Case missmatch")
else:
      print("Password mismatch")

