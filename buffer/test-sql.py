import MySQLdb

# Replace with your actual database connection details
db_host = 'localhost'
db_user = 'root'
db_password = 'password'  # Use your MySQL password here
db_database = 'persons'

try:
    # Attempt to connect to the database
    connection = MySQLdb.connect(host=db_host, user=db_user, password=db_password, database=db_database)
    cursor = connection.cursor()

    # Execute a simple query
    cursor.execute("SELECT VERSION()")

    # Fetch the result
    version = cursor.fetchone()
    print("MySQL Server Version:", version)

    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as e:
    print("Error connecting to MySQL server:", e)
