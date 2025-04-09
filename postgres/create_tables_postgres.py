import logging
import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    try:
        """ create a database connection to database """
        conn = psycopg2.connect(host="localhost", port="5432", database="student_grades",
                                user="postgres", password="pass")
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")


def create_tables(conn, sql_expression: str):
    """ create a table from the create_table_sql statement
    :param sql_expression:
    :param conn: Connection object
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except psycopg2.DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    # read the file with the script to create the tables
    with open('create_table_postgres.sql', 'r') as f:
        sql = f.read()

    try:
        with create_connection() as conn:
            if conn is not None:
                create_tables(conn, sql)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)