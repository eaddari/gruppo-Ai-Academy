class School:
    def __init__(self):
        self.classrooms = {}

    def add_student(self, classroom_name, student):
        if classroom_name not in self.classrooms:
            self.classrooms[classroom_name] = []
        self.classrooms[classroom_name].append(student)

    def list_students(self):
        for classroom, students in self.classrooms.items():
            print(f"Classroom: {classroom}, Students: {sorted([f"{student['name']} {student['surname']}" for student in students])}")

    def find_student(self, student_name):
        for classroom, students in self.classrooms.items():
            if any(student['name'].lower() in student_name.lower() for student in students):
                print(f"Found in {classroom}")
                break
        else:
            print("Student not found.")