import logging
from faker import Faker
from random import randint
from connect_sqlite import create_connection
from sqlite3 import DatabaseError


NUMBER_GROUPS = 3
NUMBER_STUDENTS = 50
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 1000  # NUMBER_STUDENTS*20


def generate_fake_data(number_groups, number_teachers, number_students,
                       number_subjects, number_grades) -> tuple:
    fake_groups = []
    fake_students = []
    fake_teachers = []
    fake_subjects = []
    fake_dates = []

    fake_data = Faker('uk-Ua')

    # Create a set of groups in the amount number_groups
    for _ in range(number_groups):
        fake_groups.append(fake_data.word())

    # Generate number_teachers teachers
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    # Generate number_students students
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Generate number_subjects subjects
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.word())

    # Generate fake dates
    for _ in range(number_grades):
        fake_dates.append(fake_data.date_this_decade().strftime("%Y-%m-%d"))

    return fake_groups, fake_teachers, fake_students, fake_subjects, fake_dates


def prepare_data(groups, teachers, students, subjects, dates) -> tuple:
    for_groups = []
    # Preparing a list of group name tuples
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    # Preparing a list of teacher name tuples
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_students = []  # for table students

    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_subjects = []  # for table subjects

    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_grades = []  # for table grades

    for grade_date in dates:
        for_grades.append((randint(1, NUMBER_STUDENTS), randint(1, NUMBER_SUBJECTS),
                           randint(0,100), grade_date))

    return for_groups, for_teachers, for_students, for_subjects, for_grades


def insert_data(conn, sql_expression: str, data):
    c = conn.cursor()
    try:
        c.executemany(sql_expression, data)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


def insert_data_to_db(groups, teachers, students, subjects, grades) -> None:
    # Create a connection to our database and get a cursor object for data manipulation
    try:
        with create_connection() as con:

            cur = con.cursor()

            sql_to_groups = """INSERT INTO groups(name) VALUES (?)"""

            '''To insert all the data at once, we will use the executemany cursor method.
            The first parameter will be the script text, and the second will be the data
            (a list of tuples).'''

            insert_data(con, sql_to_groups, groups)

            sql_to_teachers = """INSERT INTO teachers(fullname) VALUES (?)"""

            insert_data(con, sql_to_teachers, teachers)

            # Insert student data

            sql_to_students = """INSERT INTO students(fullname, group_id)
                                  VALUES (?, ?)"""

            # The data has been prepared in advance, so we just pass it to the function

            insert_data(con, sql_to_students, students)

            sql_to_subjects = """INSERT INTO subjects(name, teacher_id)
                                  VALUES (?, ?)"""

            insert_data(con, sql_to_subjects, subjects)

            sql_to_grades = """INSERT INTO grades(student_id, subject_id, grade, grade_date)
                                VALUES (?, ?, ?, ?)"""

            insert_data(con, sql_to_grades, grades)

    except RuntimeError as err:
        logging.error(err)


if __name__ == "__main__":
    f_groups, f_teachers, f_students, f_subjects, f_grades = \
        prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_TEACHERS,
                                         NUMBER_STUDENTS, NUMBER_SUBJECTS, NUMBER_GRADES))
    insert_data_to_db(f_groups, f_teachers, f_students, f_subjects, f_grades)
