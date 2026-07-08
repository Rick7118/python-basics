students = {}

while True:
    print("Choose your action")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update CGPA")
    print("4. Exit")

    choice =  input("Enter your choice: ")

    if choice == "1":
        
        name = input("Enter student name: ")
        cgpa = float(input("Enter CGPA: "))

        students[name] = cgpa

    elif choice == "2":

        name = input("Enter student's name: ")
        print(students.get(name,"Student not in database"))

    elif choice == "3":

        name = input("Enter student's name: ")

        if students.get(name) is None:
            print("Student does not exist")
        else:
            students[name] = float(input("Enter updated CGPA: "))

    elif choice == "4":
        break

    else:
        print("Choose a valid option")


    





