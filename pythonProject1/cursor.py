import psycopg2
from psycopg2 import OperationalError
def cursor(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
            print(f"The error '{e}' occurred")
    return connection.cursor()
cursor(
    "postgres", "postgres", "mayday", "127.0.0.1", "5432"
)

