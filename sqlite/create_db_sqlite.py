import sqlite3


def create_db():
    # read the file with the script to create the database
    with open('create_table_sqlite.sql', 'r') as f:
        sql = f.read()

    # create a connection to the database (if the database file does not exist, it will be created)
    with sqlite3.connect('student_grades.sqlite') as con:
        cur = con.cursor()
        # execute a script from a file that will create tables in the database
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()