import logging
from psycopg2 import DatabaseError
from connect_postgres import create_connection


if __name__ == '__main__':
    with open('../queries/query_12.sql', 'r') as f:
        sql = f.read()
    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql)
                    results = c.fetchall()
                    for res in results:
                        print(res)
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)