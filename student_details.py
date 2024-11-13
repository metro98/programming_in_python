
info_dict = {}
for i in range(3):

    student_name = input("Enter the student name: ")

    student_roll = int(input("Enter student roll number: "))

    student_department = input("Enter student department: ")

    info_dict[student_name] = {"Roll no": student_roll,
                           "Name" : student_name,
                           "Dept" : student_department}





print(info_dict)