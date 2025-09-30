import psycopg2

DB_CONFIG = {
    'host': 'my_postgres',
    'port': 5432,
    'database': 'mydatabase',
    'user': 'user',
    'password': 'password',
}

def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn
