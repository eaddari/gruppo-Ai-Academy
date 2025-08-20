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
            print(
                f"Classroom: {classroom}, Students: {sorted([f'{student["name"]} {student["surname"]}' for student in students])}"
            )

    def find_student(self, student_name: str) -> None:
        """
        Find a student by name.

        Parameters
        ----------
        student_name : str
            The APPROXIMATE name of the student to find.
        """
        found = False
        search = student_name.strip().lower()
        for classroom, students in self.classrooms.items():
            for student in students:
                full_name = (student["name"] + " " + student["surname"]).strip().lower()
                if search in full_name or full_name in search:
                    print(
                        f"Found: {student['name']} {student['surname']} in {classroom}"
                    )
                    found = True
        if not found:
            print("Student not found.")
