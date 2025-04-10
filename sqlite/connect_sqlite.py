import sqlite3
from contextlib import contextmanager


@contextmanager
def create_connection():
    try:
        """ create a database connection to database """
        conn = sqlite3.connect('student_grades.sqlite')
        yield conn
        conn.close()
    except sqlite3.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")