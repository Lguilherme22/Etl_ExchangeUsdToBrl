import psycopg2
from typing import Dict,Union

DB_CONFIG:Dict[str,Union[str,int]] = {
    'host': 'my_postgres',
    'port': 5432,
    'database': 'mydatabase',
    'user': 'user',
    'password': 'password',
}

def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn
