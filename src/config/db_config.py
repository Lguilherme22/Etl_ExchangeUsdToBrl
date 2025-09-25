import psycopg2

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'exchange',
    'user': 'lrosa',
    'password': 'root',
}

def get_connection():
    conn = psycopg2.connect(DB_CONFIG)
    return conn
