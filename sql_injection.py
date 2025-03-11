# sql_injection.py

import sqlite3

def get_user_data(user_id):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    
    # Insecure: SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    
    result = cursor.fetchall()
    connection.close()
    return result

if __name__ == "__main__":
    user_id = input("Enter user ID: ")
    user_data = get_user_data(user_id)
    print(f"User data: {user_data}")
