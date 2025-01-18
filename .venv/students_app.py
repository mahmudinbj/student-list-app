# Student List App

students = []


def add_student():
    name = input("Enter student's name: ")
    address = input("Enter student's address: ")
    grade = input("Enter student's grade: ")
    student = {"name": name, "address": address, "grade": grade}
    students.append(student)
    print(f"Student '{name}' added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return
    print("\nStudent List:")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student['name']}, Address: {student['address']}, Grade: {student['grade']}")
    print()


def delete_student():
    if not students:
        print("No students found.\n")
        return
    name_to_delete = input("Enter the name of the student to delete: ")
    for student in students:
        if student["name"].lower() == name_to_delete.lower():
            students.remove(student)
            print(f"Student '{name_to_delete}' deleted successfully!\n")
            return
    print(f"No student found with the name '{name_to_delete}'.\n")


def main():
    while True:
        print("Student List App")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the app
main()
