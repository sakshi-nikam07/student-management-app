
import os
import sqlite3


def get_student(student_id: int):
    """Fetch a student by ID from the database."""
    database_path = os.environ.get("STUDENT_DB_PATH", "students.db")

    with sqlite3.connect(database_path) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id, name FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

    return dict(student) if student else None


if __name__ == "__main__":
    result = get_student(1)
    print(result)
