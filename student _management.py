students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "D"

        student = {
            "name": name,
            "roll": roll,
            "marks": marks,
            "grade": grade
        }

        students.append(student)
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found")
        else:
            print("\nStudent Records")
            for s in students:
                print("---------------------------")
                print("Name :", s["name"])
                print("Roll :", s["roll"])
                print("Marks:", s["marks"])
                print("Grade:", s["grade"])

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        found = False
        for s in students:
            if s["roll"] == roll:
                print("\nStudent Found")
                print("Name :", s["name"])
                print("Roll :", s["roll"])
                print("Marks:", s["marks"])
                print("Grade:", s["grade"])
                found = True

        if not found:
            print("Student Not Found")

    elif choice == "4":
        roll = input("Enter Roll Number to Update: ")

        found = False
        for s in students:
            if s["roll"] == roll:
                s["name"] = input("Enter New Name: ")
                s["marks"] = float(input("Enter New Marks: "))

                if s["marks"] >= 90:
                    s["grade"] = "A"
                elif s["marks"] >= 75:
                    s["grade"] = "B"
                elif s["marks"] >= 60:
                    s["grade"] = "C"
                else:
                    s["grade"] = "D"

                print("Student Updated Successfully")
                found = True

        if not found:
            print("Student Not Found")

    elif choice == "5":
        roll = input("Enter Roll Number to Delete: ")

        found = False
        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                print("Student Deleted Successfully")
                found = True
                break

        if not found:
            print("Student Not Found")

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")