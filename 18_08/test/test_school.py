from src.school import School


def test_add_student():
    school = School()

    student = {"name": "Alice", "surname": "Smith"}
    school.add_student("1A", student)

    assert "1A" in school.classrooms
    assert school.classrooms["1A"][0] == student


def test_list_students_prints_sorted_names(capsys):
    school = School()

    school.add_student("1A", {"name": "Bob", "surname": "Brown"})
    school.add_student("1A", {"name": "Alice", "surname": "Smith"})

    school.list_students()

    captured = capsys.readouterr()

    assert "Classroom: 1A, Students: ['Alice Smith', 'Bob Brown']" in captured.out


def test_find_student_found(capsys):
    school = School()

    school.add_student("2B", {"name": "Charlie", "surname": "Doe"})
    school.find_student("Charlie")

    captured = capsys.readouterr()

    assert "Found: Charlie Doe in 2B" in captured.out


def test_find_student_not_found(capsys):
    school = School()

    school.add_student("3C", {"name": "Diana", "surname": "Evans"})
    school.find_student("Eve")

    captured = capsys.readouterr()

    assert "Student not found." in captured.out
