from sqlalchemy import create_engine

# Establishing a connection to the database
engine = create_engine('mysql+mysqlconnector://your_username:your_password@localhost/your_database')

# Creating a stored procedure
def create_stored_procedure():
    with engine.connect() as connection:
        try:
            connection.execute("""
            CREATE PROCEDURE GetCustomers()
            BEGIN
                SELECT * FROM customers;
            END
            """)
            print("Stored procedure created successfully.")
        except Exception as error:
            print(f"Error creating stored procedure: {error}")

# Calling the stored procedure
def call_stored_procedure():
    with engine.connect() as connection:
        try:
            result = connection.execute("CALL GetCustomers()")
            rows = result.fetchall()
            for row in rows:
                print(row)
        except Exception as error:
            print(f"Error calling stored procedure: {error}")

# Create the stored procedure
create_stored_procedure()

# Call the stored procedure
call_stored_procedure()
