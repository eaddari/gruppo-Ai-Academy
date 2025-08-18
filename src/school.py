class School:
    """
    A class to represent a school with multiple classrooms.
    """
    classrooms: dict[str, list[dict[str, str]]]
    def __init__(self):
        self.classrooms = {}

    def add_student(self, classroom_name: str, student: dict[str, str]) -> None:
        """Add a student to a classroom.

        Parameters
        ----------
        classroom_name : str
            The name of the classroom to add the student to.

        student : dict[str, str]
            A dictionary containing the student's information (name and surname).
        """


        if classroom_name not in self.classrooms:
            self.classrooms[classroom_name] = []
        self.classrooms[classroom_name].append(student)

    def list_students(self) -> None:
        """
        List all students in each classroom.
        """
        for classroom, students in self.classrooms.items():
            print(f"Classroom: {classroom}, Students: {sorted([f"{student['name']} {student['surname']}" for student in students])}")

    def find_student(self, student_name: str) -> None:
        """
        Find a student by name.

        Parameters
        ----------
        student_name : str
            The APPROXIMATE name of the student to find.
        """
        for classroom, students in self.classrooms.items():
            if any(student['name'].lower() in student_name.lower() for student in students):
                print(f"Found in {classroom}")
                break
        else:
            print("Student not found.")