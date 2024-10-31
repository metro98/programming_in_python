days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours_list = []
for day in days:
    number_of_hours = int(input(f"Enter the number of hours worked on {day}:"))
    hours_list.append(number_of_hours)

sum_of_hours = sum(hours_list)
print(hours_list)
print(sum_of_hours)

hourly_wage = float(input("Enter the hourly wage: "))
total_earnings = hourly_wage * sum_of_hours
print(f"Your total earnings is {round(total_earnings,2)}")
