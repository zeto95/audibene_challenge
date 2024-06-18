# utils.py
import os
import requests
import sqlite3

GITHUB_API_URL = "https://api.github.com/repos/psf/requests"
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}"
}

def fetch_data(endpoint):
    url = f"{GITHUB_API_URL}/{endpoint}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_data(conn, table_name, data, columns):
    sql = f"INSERT OR IGNORE INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['?'] * len(columns))})"
    cur = conn.cursor()
    for row in data:
        values = [row[i] for i in range(len(columns))]  # Access tuple elements using integer indices
        cur.execute(sql, values)
    conn.commit()
