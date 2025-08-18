from src.student_manager import School

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
            except ValueError:
                print("Invalid input. Please enter valid strings.")
                continue
            
            school.add_student(classroom_name, student)
            print("Student added.")

        elif main_menu == '2':
            school.list_students()

        elif main_menu == '3':
            student_name = input("Enter student's name to search: ")
            school.find_student(student_name)

        elif main_menu == 'exit':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()