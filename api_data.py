# api_data.py
import os
from utils import fetch_data, create_connection, create_table, insert_data

DATABASE_FILE = 'raw_data.db'

def store_commits(commits, conn):
    create_table_sql = '''CREATE TABLE IF NOT EXISTS commits (
                            sha TEXT PRIMARY KEY,
                            author TEXT,
                            message TEXT,
                            date TEXT
                        )'''
    create_table(conn, create_table_sql)
    columns = ['sha', 'author', 'message', 'date']
    data = [(commit['sha'], commit['commit']['author']['name'], commit['commit']['message'], commit['commit']['author']['date']) for commit in commits]
    insert_data(conn, 'commits', data, columns)

def store_issues(issues, conn):
    create_table_sql = '''CREATE TABLE IF NOT EXISTS issues (
                            id INTEGER PRIMARY KEY,
                            title TEXT,
                            state TEXT,
                            created_at TEXT,
                            updated_at TEXT,
                            closed_at TEXT
                        )'''
    create_table(conn, create_table_sql)
    columns = ['id', 'title', 'state', 'created_at', 'updated_at', 'closed_at']
    data = [(issue['id'], issue['title'], issue['state'], issue['created_at'], issue['updated_at'], issue['closed_at']) for issue in issues]
    insert_data(conn, 'issues', data, columns)

def main():
    # Fetch commit data
    commits = fetch_data('commits')
    # Fetch issue data
    issues = fetch_data('issues')

    # Connect to SQLite database
    conn = create_connection(DATABASE_FILE)

    # Store commits and issues in database
    store_commits(commits, conn)
    store_issues(issues, conn)

    # Close connection
    conn.close()

if __name__ == "__main__":
    main()
