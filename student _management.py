students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll Number: ")

        student = {
            "name": name,
            "roll": roll
        }

        students.append(student)
        print("Student Added Successfully!")

    elif choice == "2":
        print("\nStudent List:")
        for s in students:
            print("Name:", s["name"], "Roll:", s["roll"])

    elif choice == "3":
        search = input("Enter Roll Number: ")

        found = False
        for s in students:
            if s["roll"] == search:
                print("Name:", s["name"])
                print("Roll:", s["roll"])
                found = True

        if not found:
            print("Student Not Found")

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")