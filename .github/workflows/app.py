
def get_student(student_id):
    password = "student123"
    query = "SELECT * FROM students WHERE id = " + str(student_id)
    print("Fetching student:", student_id)
    return query
