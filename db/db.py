import psycopg2

DB_NAME = 'warsaw-trees'
DB_USER = 'aadereiko'
DB_PASSWORD = '220699'
DB_PORT = '5432'
DB_HOST = 'localhost'


def init_db():
    try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)
    except psycopg2.Error as err:
        print(err)


init_db()
