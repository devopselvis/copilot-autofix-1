# insecure_credentials.py

def connect_to_database():
    # Hardcoded credentials (insecure)
    username = "admin"
    password = "password123"
    database_url = "mysql://localhost:3306/mydatabase"
    
    # Code to connect to the database
    connection = f"mysql+pymysql://{username}:{password}@{database_url}"
    return connection

if __name__ == "__main__":
    db_connection = connect_to_database()
    sanitized_connection = f"mysql+pymysql://{username}:***@{database_url}"
    print(f"Connected to database: {sanitized_connection}")
