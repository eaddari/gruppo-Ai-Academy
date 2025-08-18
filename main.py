from src.school import School

def main():

    school = School()

    while True:
        main_menu = input("Enter 1 to add a student to a classroom, 2 to list students, 3 to look for a student, or 'exit' to quit: ")

        if main_menu == '1':
            try:
                classroom_name = input("Enter classroom name: ")
                student = {}
                student['name'] = input("Enter student's name: ")
                student['surname'] = input("Enter student's surname: ")
                school.add_student(classroom_name, student)
                print("Student added.")
            except Exception as e:
                print(f"Error adding student: {e}")

        elif main_menu == '2':
            try:
                school.list_students()
            except Exception as e:
                print(f"Error listing students: {e}")

        elif main_menu == '3':
            try:
                student_name = input("Enter student's name to search: ")
                school.find_student(student_name)
            except Exception as e:
                print(f"Error finding student: {e}")

        elif main_menu == 'exit':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()