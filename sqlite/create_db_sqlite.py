import logging
from sqlite3 import DatabaseError
from connect_sqlite import create_connection


def create_tables(conn, sql_expression: str):
    """ create a table from the create_table_sql statement
    :param sql_expression:
    :param conn: Connection object
    :return:
    """
    c = conn.cursor()
    try:
        c.executescript(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == "__main__":
    # read the file with the script to create the tables
    with open('create_table_sqlite.sql', 'r') as f:
        sql = f.read()

    try:
        with create_connection() as conn:
            if conn is not None:
                create_tables(conn, sql)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)